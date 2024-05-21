import bpy
import math
import random

# Paramètres de la spirale
n = 3000  # Nombre d'objets
a = 0.02  # Spirale size
b = 0.01  # Spirale radius
d = 0.01  # Random location "radius"
o = 0.15   # Angle

# Supprimer tous les objets existants
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

mat_star = bpy.data.materials.get("Star")

# Créer une spirale d'objets sphériques
for i in range(n):
    theta = i * math.pi * o  # Angle
    r = a * math.exp(b * theta)  # Rayon
    x = r * math.cos(theta)  # Coordonnée x
    y = r * math.sin(theta)  # Coordonnée y
    
    # Random
    x = x + (((random.random()-.5)*i) * d)
    y = y + (((random.random()-.5)*i) * d)

    # Créer un nouvel objet sphérique à la position (x, y, 0)
    bpy.ops.mesh.primitive_plane_add(size=0.05, location=(x, y, 0))
    bpy.context.active_object.data.materials.append(mat_star)
