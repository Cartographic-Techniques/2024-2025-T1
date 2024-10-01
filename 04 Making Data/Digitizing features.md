#How to Digitize Features (Points, Lines, and Polygons) in QGIS

Digitizing is the process of converting features from a map or an image into vector data, such as points, lines, or polygons. This tutorial will guide you through digitizing features in QGIS.

### Step 1: Load or Create a New Vector Layer
Before digitizing features, you need a vector layer (for points, lines, or polygons) to store the data.

1. **Create a New Layer Scratch**:
   - Go to `Layer > Create Layer > New Temporary Scratch Layer`.
   - In the `New Temporary Scratch Layer` dialog box:
     - Choose `Point`, `Line`, or `Polygon` depending on what type of feature you want to digitize.
     - Set the `Coordinate Reference System (CRS)` to match your project or the CRS of your basemap (e.g., `EPSG:4326` for WGS 84).
     - Add any attribute fields you want.

### Step 2: Toggle Editing Mode
1. Select the layer you want to edit from the `Layers Panel`.
2. Click the `Toggle Editing` button (pencil icon) in the toolbar or right-click the layer in the Layers Panel and select `Toggle Editing`. This allows you to start modifying the layer.

### Step 3: Digitize Features

#### A. **Digitizing Points**
1. Ensure you are working with a `Point` layer.
2. Click the `Add Point Feature` button (the point icon) in the toolbar.
3. Click on the map where you want to place a point. 
4. A dialog will pop up prompting you to enter attribute information (e.g., name, type). Fill out the fields and click `OK`.
5. Repeat for each point you want to digitize.

#### B. **Digitizing Lines**
1. If you're working with a `Line` layer, click the `Add Line Feature` button (the line icon).
2. Click on the map to start drawing a line. Each click places a vertex, and the line will continue to form as you click.
3. To complete the line, right-click (or double-click) after placing the last point.
4. Enter the attribute data (if applicable) and click `OK`.

#### C. **Digitizing Polygons**
1. If you're working with a `Polygon` layer, click the `Add Polygon Feature` button (the polygon icon).
2. Click on the map to start drawing the polygon. Each click adds a vertex to form the edges.
3. To finish the polygon, right-click (or double-click) after placing the last vertex.
4. Enter the attribute data in the popup and click `OK`.

### Step 4: Modify Features (Optional)

1. **Move a Feature**: To adjust the position of a point, line, or polygon, click the `Vertex Tool` and drag the vertices to modify the feature.
2. **Delete a Feature**: Select the feature you want to remove, then click the `Delete Selected` button (trash icon).
3. **Edit Attributes**: Right-click on a feature, select `Open Attribute Table`, and edit the values in the table.

### Step 5: Save Edits and Toggle Editing Off
1. Once you've finished digitizing, click the `Save Layer Edits` button (disk icon) in the toolbar to save your changes.
2. Toggle `Editing Mode Off` by clicking the `Toggle Editing` button again. This will lock the layer and prevent further modifications.

### Step 7: Export the Digitized Layer (Optional)
Temporary scratch layers are not saved, and will be discarded when QGis is closed.
If you want to reuse your digitized layer in the future, you have to save it as a new file:

1. Right-click the layer in the Layers Panel and choose `Export > Save Features As`.
2. Select the format you want to save it in (e.g., `Shapefile`, `GeoJSON`, etc.).
3. Set the output file name and click `OK`.