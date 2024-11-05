import bpy

# Get the material and image texture node
material = bpy.data.materials.get("Material_displacement")  # Replace with your material's name
if not material:
    raise ValueError("Material not found.")

# Ensure the material has nodes
material.use_nodes = True
nodes = material.node_tree.nodes

# Find the Image Texture node
image_node = nodes.get("Image Texture")  # Replace with the name of your Image Texture node
if not image_node:
    raise ValueError("Image Texture node not found.")

# Ensure the image node has an image loaded
image = image_node.image
if not image:
    raise ValueError("No image found in Image Texture node.")

# Get image dimensions
img_width, img_height = image.size
aspect_ratio = img_width / img_height

# Define the target objects
plane = bpy.data.objects["Plane"]  # Replace "Plane" with the actual name of your plane object
camera = bpy.data.objects["Camera"]  # Replace "Camera" with the actual name of your camera object

# 1. Scale the plane to match the image aspect ratio
if aspect_ratio >= 1:
    plane.scale[0] = aspect_ratio
    plane.scale[1] = 1
else:
    plane.scale[0] = 1
    plane.scale[1] = 1 / aspect_ratio

# 2. Set render resolution to match the image dimensions
scene = bpy.context.scene
scene.render.resolution_x = img_width
scene.render.resolution_y = img_height

# 3. Set camera orthographic scale (twice the greater of width or height in the aspect ratio)
max_dimension = max(img_width, img_height)
camera.data.ortho_scale = max_dimension / min(img_width, img_height) * 2
