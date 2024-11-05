# Blender Tutorial: Modifying the Shaded Relief Template

A more detailed tutorial about shaded reliefs and Blender can be found here: https://somethingaboutmaps.wordpress.com/2017/11/16/creating-shaded-relief-in-blender/ 


### Step 1: Select the Plane in the Scene

1. **Open Blender**: Launch Blender and open your existing project file that contains the plane.

2. **Select the Plane**:
   - In the 3D Viewport (the main window where you see your 3D objects), navigate to the plane you want to work with.
   - Left-click on the plane to select it. You should see an orange outline around it, indicating that it is selected.

### Step 2: Open the Shader Editor

The Shader Editor is a workspace in Blender that allows you to create and modify materials for your 3D objects. It provides a node-based interface, where you can connect different nodes to define how surfaces react to light and what textures they display.

1. **Switch to the Shader Editor**:
   - At the top of your Blender interface, you will see various workspace tabs (like Layout, Modeling, etc.). Click on the “Shading” tab.
   - This will split your screen and bring up the Shader Editor at the bottom.

### Step 3: Load a New Image in the "Image Texture" Node

1. **Locate the Image Texture Node**:
   - In the Shader Editor, look for the "Image Texture" node. It should already be present as part of the material assigned to your plane.

2. **Load a New Image**:
   - Click on the "Image Texture" node to select it.
   - Click on the folder icon close to the image name.
   - Navigate to the location on your computer where the desired image is saved, select it, and click “Open Image.”
   - The new image will now be loaded into the material of the plane.

### Step 4: Open the Text Editor

The Text Editor in Blender allows you to write and execute scripts using Python, which can automate tasks or modify properties in your scene.

1. **Open the Scripting Editor**:
   - To access the Text Editor, go to the top of the Blender interface and click on the “+” icon next to the existing workspace tabs.
   - From the dropdown menu, choose “Scripting.” This will create a new area in your interface where you can write or run scripts.

### Step 5: Run the Script that is Open

1. **Ensure Your Script is Open**:
   - If a script is already open in the Text Editor, review it briefly to understand what it does. If you need to load a different script, click “Open” in the Text Editor and select the desired Python script file.

2. **Run the Script**:
   - To execute the script, make sure the Text Editor window is active (click on it if necessary).
   - At the top of the Text Editor, click on the “Run Script” button, which looks like a play icon. Alternatively, you can press `Alt + P` on your keyboard while your cursor is in the Text Editor to run the script.

This Python script adjusts the material and camera to render the new DEM with accurate proportions. Using the DEM's dimensions, it scales the plane object to match the image’s aspect ratio, sets the render resolution to the image's size, and adjusts the camera’s orthographic scale so the image fills the view accurately when rendered.

Here is a more detailed outline of the code:

1. **Locate Material and Texture**: It retrieves a material named "Material_displacement" and checks if it has an "Image Texture" node with an image loaded. If not, it raises an error.
  
2. **Get Image Dimensions and Aspect Ratio**: The code reads the dimensions (width and height) of the image associated with the "Image Texture" node and calculates its aspect ratio.

3. **Scale a Plane Object**: It scales a specified plane object ("Plane") to match the aspect ratio of the image. If the image is wider than it is tall, it scales the plane's width; if the image is taller, it scales the plane's height.

4. **Set Render Resolution**: The script adjusts the scene’s render resolution to match the image’s dimensions, ensuring the render matches the image’s size.

5. **Set Camera’s Orthographic Scale**: For a camera object ("Camera"), it sets the orthographic scale based on the larger dimension of the image, ensuring that the image fills the camera's view when rendered.



 