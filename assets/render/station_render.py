#!/usr/bin/env python3
"""Blender scene of the autodissemination Station, built to the dimensions in
phase5-device-design.md §3. Run headless:

    blender -b -P assets/render/station_render.py -- --out assets/render --samples 128

or with the `bpy` pip module (python3 -m pip install bpy):

    python3 assets/render/station_render.py --out assets/render

Produces: station-hero.png (3/4 view), station-section.png (cut-away showing the
lure, vanes, sun collar and velvet sleeve), station-field.png (four Stations in an
onion plot) and station.blend for editing.

All dimensions are metres. Z is up. Soil is z = 0.
"""
import math
import sys
import argparse
from pathlib import Path

import bpy
import bmesh
from mathutils import Vector

# ----------------------------------------------------------------- dimensions
HOOD_D = 0.400          # P1 basin diameter
HOOD_DEPTH = 0.100      # P1 basin depth
HOOD_WALL = 0.003
TUBE_OD = 0.110         # P5 4-inch PVC
TUBE_ID = 0.102
TUBE_L = 0.200          # P5
COLLAR = 0.050          # P6 plain sun collar
SLEEVE_H = 0.150        # P7 velvet sleeve
WINDOW = 0.080          # entry window, hood rim to tube top
VANE = 0.100            # P4 100 x 100 mm, 20 mm into the tube
VANE_T = 0.004
ROD_D = 0.003           # P9
CAGE_D, CAGE_H = 0.035, 0.050   # P3
HANGER_L = 0.200        # P2 M6 rod
TUBE_BOTTOM_Z = 0.600   # mount height
POLE_D = 0.030          # bamboo / 1" PVC
POLE_L = 1.200          # 0.30 buried
LURE_ABOVE_VANES = 0.090

TUBE_TOP_Z = TUBE_BOTTOM_Z + TUBE_L
HOOD_RIM_Z = TUBE_TOP_Z + WINDOW
HOOD_CROWN_Z = HOOD_RIM_Z + HOOD_DEPTH

# ----------------------------------------------------------------- helpers
def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def mat(name, rgb, rough=0.5, metal=0.0, spec=0.5, alpha=1.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*rgb, 1)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = spec
    if alpha < 1:
        bsdf.inputs["Alpha"].default_value = alpha
        m.blend_method = "BLEND"
    return m


def link(obj, coll=None):
    (coll or bpy.context.scene.collection).objects.link(obj)
    return obj


def cylinder(name, r, h, z0, material, verts=96, r_in=None, coll=None):
    """Solid cylinder, or a tube when r_in is given, from z0 to z0+h."""
    bm = bmesh.new()
    if r_in is None:
        bmesh.ops.create_cone(bm, cap_ends=True, segments=verts, radius1=r, radius2=r, depth=h)
    else:
        outer = bmesh.ops.create_circle(bm, cap_ends=False, segments=verts, radius=r)
        inner = bmesh.ops.create_circle(bm, cap_ends=False, segments=verts, radius=r_in)
        # bridge the two rings, then extrude
        bmesh.ops.bridge_loops(bm, edges=[e for e in bm.edges])
        faces = list(bm.faces)
        res = bmesh.ops.extrude_face_region(bm, geom=faces)
        up = [v for v in res["geom"] if isinstance(v, bmesh.types.BMVert)]
        bmesh.ops.translate(bm, vec=(0, 0, h), verts=up)
        bmesh.ops.translate(bm, vec=(0, 0, -h / 2), verts=bm.verts)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    ob.location.z = z0 + h / 2
    ob.data.materials.append(material)
    for p in me.polygons:
        p.use_smooth = True
    link(ob, coll)
    return ob


def box(name, sx, sy, sz, loc, material, rot=(0, 0, 0), coll=None):
    bpy.ops.mesh.primitive_cube_add(size=1)
    ob = bpy.context.object
    ob.name = name
    ob.scale = (sx, sy, sz)
    ob.location = loc
    ob.rotation_euler = rot
    ob.data.materials.append(material)
    return ob


def rod(name, p0, p1, r, material, coll=None):
    d = Vector(p1) - Vector(p0)
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=r, depth=d.length)
    ob = bpy.context.object
    ob.name = name
    ob.location = (Vector(p0) + Vector(p1)) / 2
    ob.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    ob.data.materials.append(material)
    for p in ob.data.polygons:
        p.use_smooth = True
    return ob


def hood(material):
    """Inverted PP basin: a slightly tapered shell with a rolled rim."""
    bm = bmesh.new()
    r_top = HOOD_D / 2 * 0.86
    r_rim = HOOD_D / 2
    prof = [(r_rim, 0), (r_rim, 0.012), (r_rim - 0.004, 0.012), (r_rim - 0.004, 0.004),
            (r_top, HOOD_DEPTH - HOOD_WALL), (0, HOOD_DEPTH - HOOD_WALL),
            (0, HOOD_DEPTH), (r_top + HOOD_WALL, HOOD_DEPTH), (r_rim + 0.002, 0.004), (r_rim + 0.002, 0)]
    verts = [bm.verts.new((x, 0, z)) for x, z in prof]
    edges = [bm.edges.new((verts[i], verts[i + 1])) for i in range(len(verts) - 1)]
    edges.append(bm.edges.new((verts[-1], verts[0])))
    geom = bmesh.ops.spin(bm, geom=verts + edges, cent=(0, 0, 0), axis=(0, 0, 1),
                          angle=2 * math.pi, steps=128, use_merge=True)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("Hood")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("Hood", me)
    ob.location.z = HOOD_RIM_Z
    ob.data.materials.append(material)
    for p in me.polygons:
        p.use_smooth = True
    link(ob)
    return ob


# ----------------------------------------------------------------- station
def build_station(origin=(0, 0, 0), section=False):
    ox, oy, oz = origin
    M = build_station.materials
    parts = []

    parts.append(hood(M["pp_white"]))
    tube = cylinder("Tube", TUBE_OD / 2, TUBE_L, TUBE_BOTTOM_Z, M["pvc_white"], r_in=TUBE_ID / 2)
    parts.append(tube)
    sleeve = cylinder("SporeSleeve", TUBE_ID / 2 - 0.0005, SLEEVE_H, TUBE_BOTTOM_Z,
                      M["velvet"], r_in=TUBE_ID / 2 - 0.0035)
    parts.append(sleeve)
    # sleeve stop rivets
    for i in range(3):
        a = math.radians(60 + 120 * i)
        parts.append(rod(f"Rivet{i}", (TUBE_ID / 2 * math.cos(a), TUBE_ID / 2 * math.sin(a), TUBE_BOTTOM_Z + SLEEVE_H),
                         ((TUBE_ID / 2 - 0.004) * math.cos(a), (TUBE_ID / 2 - 0.004) * math.sin(a), TUBE_BOTTOM_Z + SLEEVE_H),
                         0.002, M["steel"]))
    # cross vanes: 80 mm above the tube, 20 mm inside
    vz = TUBE_TOP_Z - 0.020 + VANE / 2
    parts.append(box("VaneA", VANE, VANE_T, VANE, (0, 0, vz), M["coroplast"]))
    parts.append(box("VaneB", VANE_T, VANE, VANE, (0, 0, vz), M["coroplast"]))
    # support rods at 120 deg, hooked into hood rim and tube top
    for i in range(3):
        a = math.radians(30 + 120 * i)
        p_tube = ((TUBE_OD / 2 + 0.002) * math.cos(a), (TUBE_OD / 2 + 0.002) * math.sin(a), TUBE_TOP_Z - 0.015)
        p_hood = ((HOOD_D / 2 * 0.86) * math.cos(a), (HOOD_D / 2 * 0.86) * math.sin(a), HOOD_CROWN_Z - 0.004)
        parts.append(rod(f"Rod{i}", p_tube, p_hood, ROD_D / 2, M["steel"]))
    # lure hanger and cage
    lure_z = TUBE_TOP_Z + VANE - 0.020 + LURE_ABOVE_VANES
    parts.append(rod("Hanger", (0, 0, lure_z), (0, 0, HOOD_CROWN_Z + 0.015), 0.003, M["steel"]))
    parts.append(cylinder("WingNut", 0.010, 0.006, HOOD_CROWN_Z + 0.001, M["steel"], verts=6))
    parts.append(cylinder("LureCage", CAGE_D / 2, CAGE_H, lure_z - CAGE_H, M["pp_grey"], verts=48))
    parts.append(cylinder("Lure", 0.006, 0.012, lure_z - CAGE_H / 2 - 0.006, M["rubber"], verts=24))
    # pole and hose clamps
    parts.append(cylinder("Pole", POLE_D / 2, POLE_L, -0.300, M["bamboo"], verts=32))
    for z in (TUBE_BOTTOM_Z + 0.030, TUBE_BOTTOM_Z + TUBE_L - 0.030):
        parts.append(cylinder(f"Clamp{z:.2f}", TUBE_OD / 2 + 0.004, 0.012, z, M["steel"], verts=64, r_in=TUBE_OD / 2 + 0.001))
    # label
    parts.append(box("Label", 0.001, 0.080, 0.050, (TUBE_OD / 2 + 0.0005, 0, TUBE_BOTTOM_Z + 0.100), M["label"]))

    # pole offset: pole sits beside the tube, clamped
    for p in parts:
        if p.name.startswith(("Pole", "Clamp")):
            pass
    pole = [p for p in parts if p.name == "Pole"][0]
    pole.location.x = -(TUBE_OD / 2 + POLE_D / 2 + 0.002)
    for p in parts:
        if p.name.startswith("Clamp"):
            p.scale.x = (TUBE_OD + POLE_D + 0.012) / (TUBE_OD + 0.008)
            p.location.x = -(POLE_D / 2 + 0.002) / 2

    if section:
        # cut away the front half of hood, tube and sleeve with a boolean
        cutter = box("Cutter", 1, 1, 2, (0, -0.5, 1), M["pp_white"])
        cutter.hide_render = True
        cutter.hide_viewport = True
        for p in parts:
            if p.name in ("Hood", "Tube", "SporeSleeve"):
                b = p.modifiers.new("Section", "BOOLEAN")
                b.operation = "DIFFERENCE"
                b.object = cutter
                b.solver = "EXACT"

    for p in parts:
        p.location.x += ox
        p.location.y += oy
        p.location.z += oz
    return parts


def materials():
    return {
        "pp_white": mat("PP white", (0.90, 0.90, 0.88), rough=0.45, spec=0.4),
        "pvc_white": mat("PVC white paint", (0.88, 0.88, 0.86), rough=0.35),
        "velvet": mat("Black velvet", (0.02, 0.02, 0.02), rough=0.95, spec=0.1),
        "coroplast": mat("Coroplast", (0.93, 0.93, 0.93), rough=0.6),
        "steel": mat("Galvanized", (0.65, 0.66, 0.68), rough=0.35, metal=0.9),
        "pp_grey": mat("PP grey", (0.25, 0.26, 0.28), rough=0.5),
        "rubber": mat("Rubber septum", (0.65, 0.20, 0.20), rough=0.7),
        "bamboo": mat("Bamboo", (0.72, 0.60, 0.35), rough=0.7),
        "label": mat("Label", (0.98, 0.98, 0.95), rough=0.5),
        "soil": mat("Soil", (0.20, 0.13, 0.08), rough=1.0, spec=0.1),
        "onion": mat("Onion leaf", (0.22, 0.45, 0.18), rough=0.6),
    }


# ----------------------------------------------------------------- environment
def ground(size=6.0):
    bpy.ops.mesh.primitive_plane_add(size=size)
    g = bpy.context.object
    g.name = "Soil"
    g.data.materials.append(build_station.materials["soil"])
    return g


def onion_plot(nx=14, ny=10, spacing=0.10, origin=(-0.7, -0.5), rows_y=0.25, skip_center=0.18):
    """Simple onion plants: tufts of tapered leaves. Rows along X at 25 cm."""
    import random
    random.seed(4)
    M = build_station.materials["onion"]
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.006, radius2=0.0, depth=0.38)
    leaf = bpy.context.object
    leaf.name = "LeafProto"
    leaf.data.materials.append(M)
    leaf.hide_render = True
    leaf.hide_viewport = True
    coll = bpy.data.collections.new("Onions")
    bpy.context.scene.collection.children.link(coll)
    for j in range(ny):
        for i in range(nx):
            x = origin[0] + i * spacing
            y = origin[1] + j * rows_y
            if abs(x) < skip_center and abs(y) < skip_center:
                continue
            for k in range(5):
                ob = leaf.copy()
                ob.hide_render = False
                ob.hide_viewport = False
                h = random.uniform(0.28, 0.42)
                ob.scale.z = h / 0.38
                tilt = random.uniform(0.15, 0.45)
                az = random.uniform(0, 2 * math.pi)
                ob.rotation_euler = (tilt * math.cos(az), tilt * math.sin(az), 0)
                ob.location = (x + random.uniform(-0.01, 0.01), y + random.uniform(-0.01, 0.01), h / 2 * math.cos(tilt))
                coll.objects.link(ob)


def lighting_and_world():
    w = bpy.context.scene.world or bpy.data.worlds.new("World")
    bpy.context.scene.world = w
    w.use_nodes = True
    nt = w.node_tree
    bg = nt.nodes["Background"]
    sky = nt.nodes.new("ShaderNodeTexSky")
    sky.sky_type = "NISHITA"
    sky.sun_elevation = math.radians(38)
    sky.sun_rotation = math.radians(210)
    sky.sun_intensity = 0.6
    sky.altitude = 20
    nt.links.new(sky.outputs[0], bg.inputs[0])
    bg.inputs[1].default_value = 0.25
    bpy.ops.object.light_add(type="SUN")
    sun = bpy.context.object
    sun.data.energy = 4.0
    sun.data.angle = math.radians(1.5)
    sun.rotation_euler = (math.radians(52), 0, math.radians(210))
    bpy.ops.object.light_add(type="AREA", location=(-1.5, -1.5, 1.6))
    fill = bpy.context.object
    fill.data.energy = 60
    fill.data.size = 1.5
    fill.rotation_euler = (math.radians(55), 0, math.radians(-45))


def camera(loc, target, lens=70, name="Camera"):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = lens
    d = Vector(target) - Vector(loc)
    cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam
    return cam


def render(path, samples, w=1600, h=1200):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.samples = samples
    sc.cycles.use_denoising = True
    sc.render.resolution_x = w
    sc.render.resolution_y = h
    sc.render.film_transparent = False
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = str(path)
    try:
        sc.cycles.device = "CPU"
    except Exception:
        pass
    bpy.ops.render.render(write_still=True)


# ----------------------------------------------------------------- main
def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=".")
    ap.add_argument("--samples", type=int, default=96)
    ap.add_argument("--quick", action="store_true", help="low-res preview")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    W, H = (800, 600) if a.quick else (1600, 1200)

    # 1. hero, 3/4 view
    clear_scene()
    build_station.materials = materials()
    ground()
    build_station()
    lighting_and_world()
    camera((1.15, -1.35, 0.95), (0, 0, 0.80), lens=85)
    render(out / "station-hero.png", a.samples, W, H)
    bpy.ops.wm.save_as_mainfile(filepath=str(out / "station.blend"))

    # 2. cut-away section
    clear_scene()
    build_station.materials = materials()
    ground()
    build_station(section=True)
    lighting_and_world()
    camera((0.05, -1.25, 0.86), (0, 0, 0.84), lens=90)
    render(out / "station-section.png", a.samples, W, H)

    # 3. field view, four Stations in an onion plot
    clear_scene()
    build_station.materials = materials()
    ground(10)
    onion_plot(nx=40, ny=18, origin=(-2.0, -2.0), skip_center=0.0)
    for (x, y) in ((0, 0), (1.5, 0.5), (-1.2, 1.4), (0.8, 2.6)):
        build_station(origin=(x, y, 0))
    lighting_and_world()
    camera((2.6, -3.2, 1.35), (0.2, 0.6, 0.55), lens=50)
    render(out / "station-field.png", a.samples, W, H)


if __name__ == "__main__":
    main()
