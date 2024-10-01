### Tutorial: How to Georeference a Map in QGIS

Georeferencing is the process of aligning spatial data (such as a scanned map) to a known coordinate system so that the data can be used in conjunction with other geospatial data. This tutorial walks through how to georeference a map in QGIS.

### Step 1: Add a Basemap for Reference

1. Go to `Plugins > Manage and Install Plugins`. Search for `QuickMapServices` and install it if you haven't already.
2. Once installed, go to the `Web` menu and select `QuickMapServices > Settings`. In the settings window, click `More Services` and then click `Get Contributed Pack` to access more basemap options.
3. Now, go to `Web > QuickMapServices`, choose a basemap from the list (e.g., `Google Satellite`, `OpenStreetMap`, etc.), and it will load directly into your map canvas.

### Step 2: Load the Image into the Georeferencer
1. Go to `layer > Georeferencer`.
2. In the Georeferencer window, click the `Open Raster` button (the folder icon in the toolbar).
3. Select your map/image file and click `Open`.

Your image should now appear in the Georeferencer window.

### Step 3: Adding Ground Control Points (GCPs)
Ground Control Points (GCPs) are specific locations on the image with known coordinates that allow QGIS to align the image with the map projection.

1. Click on the `Add Point` button (crosshair icon in the toolbar).
2. Select a **recognizable point** on your map (e.g., a road intersection, building corner, or geographical feature) and click on it.
3. A dialog box will pop up asking for the coordinates of that point. You have two options to input coordinates:
   - `Manual Entry`: If you know the exact coordinates of the point, you can enter them manually.
   - `From Map Canvas`: If you don't have the exact coordinates, but have an existing map or layer in QGIS, click on the `From Map Canvas` button and choose the corresponding point from a layer already in the correct CRS.
4. Repeat this process for at least **4-5 points** evenly distributed across your map. The more points you add (especially distributed across the entire map), the better the georeferencing accuracy.

### Step 4: Modify Settings
1. In the `Georeferencer window`, click on the `Settings` menu. 
2. Set the `Transformation type` to `Polynomial 1` (or `Thin Plate Spline` for more complex warping if needed).
3. In the `Target CRS` dropdown, select the coordinate reference system (CRS) you want to georeference your map to. For example, use `EPSG:4326` (WGS 84) for global maps or local CRS depending on your area of interest.
4. Set the `Resampling Method` (choose `Nearest neighbor` for categorical data like scanned maps, or `Cubic` for images with continuous data like satellite images).
5. Choose the location to `Save the output raster`.
6. Click `OK`.

### Step 5: Perform the Georeferencing
1. After adding all necessary points, go to the `Georeferencer window` and click the `Start Georeferencing` button (green play icon).
2. The Georeferencer will perform the transformation and create a new georeferenced raster file based on the settings you chose earlier.

---

### Tips for Better Georeferencing:
- **Accuracy of GCPs**: Try to choose points that are easily identifiable and match between the image and the reference map.
- **Even Distribution of GCPs**: Distribute GCPs evenly across the map to avoid distortions in any specific area.
- **Reference Layers**: If possible, use reference layers (e.g., shapefiles or other georeferenced maps) to pick points directly from the map canvas.