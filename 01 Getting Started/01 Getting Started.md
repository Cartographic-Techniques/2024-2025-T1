#### Objectives
* start and save a map project,
* add vector- and raster-based spatial data to the map project,
* access the Attribute Table of a vector layer,
* export a map trough the Print Layout

## Setting up QGIS
Begin to familiarize yourself with the interface. Yours may not exactly resemble the layout shown above. For instance, most toolbars and panels are movable, allowing you to set up your workspace as you like. You can always add or remove these elements of the workspace by clicking through `View > Panels or Toolboars` (from the main menu bar).

This is a brief description of the main elements of the QGIS interface. 
The QGIS Interface


1. **The Menu Bar:** This is a standard menu bar that gives you access to many elements of the software. Note that many of the items you can access here can also be accessed through the icons on the toolbars below.
2. **Toolbar:** Gives access to many commonly used tools and features in QGIS. The individual toolbar segments can be moved – hover over the edge of the toolbar until a + icon appears then click and drag the tool bar. Note the location and configuration of the elements of the toolbar on your screen might not match those in this tutorial. Please feel free to move them to which ever configuration is easiest for you to work with. 
		* Note if you ever lose one element of the tool bar you can right click (control + click on Mac) in any empty zone of the toolbar area and a full list of available toolbar elements will appear.
3. **The Map View:** This is where your maps will appear, all layers activated in the layer menu (see item 4) will be visible here. 
4. **Layer menu:** This shows all of the data layers you have added to your current map project. The order of the layers in this menu determines the order in which the layers appear in the map view. The check boxes next to each layer name allows you to turn the visibility of layers on and off. By clicking a specific layer you can access properties for that layer and perform operations on that layer. This is sometimes also referred to as the Map Legend or the Table of Contents. It is not fixed, you can drag the layer menu to occupy a different space on your screen or to take up the full left hand panel.  
5. **Browser:** the browser allows you to access your computer’s file system. You can use this to drag files onto your map project.  Like the layer menu it can be moved to occupy a different space. 
6. **Status Bar:** the status bar shows the position of your cursor in the map view, the current scale and rotation of the map view, and the project’s coordinate system. 

### Install plugins

One of the great features of QGIS is its extensibility through plugins, which can add new tools and functions to your QGIS environment. Here’s a step-by-step guide to installing plugins in QGIS:


#### Step 1: Open the Plugin Manager

- Go to the top menu bar and click on `Plugins`.
- From the dropdown menu, select `Manage and Install Plugins…`. This will open the Plugin Manager window.

#### Step 2: Browse Available Plugins
In the Plugin Manager window, you will see several tabs:
 
 - `Installed`: Shows plugins currently installed on your QGIS.
 - `All`: Shows all available plugins from the QGIS repository.
 - `Not Installed`: Displays plugins that are available but not yet installed.
 - `Settings`: Configure additional repositories and other plugin settings.
 - `Installed Plugins`: Update, enable, or disable installed plugins.

#### Step 4: Search for a Plugin
In the `All` or `Not Installed` tab, use the search bar to find a specific plugin by name or browse through the list of available plugins.
  
#### Step 5: Install a Plugin
- Once you find the desired plugin, click on it to see more details on the right side of the window.
- Click the `Install Plugin` button at the bottom right of the window. The installation process will begin, and you should see a progress bar.
  
#### Step 6: Enable and Use the Plugin
- After installation, the plugin will be automatically enabled and should appear in the `Installed` tab.
- Some plugins add new menus or toolbars to QGIS, while others might need to be accessed from the `Plugins` menu.

#### Step 7: Search and Install Plugins
Following the above procedure, search and install the following plugins:

- `QuickMapServices` (Easy to add basemaps and geoservices)
- `QuickOSM` (Download Open Street Map data thanks to the Overpass API)


#### Tips
- **Enable or disable plugins**: go to the `Installed` tab, find the plugin, and check or uncheck the box next to its name.
- **Update a plugin**: check if updates are available in the `Installed` tab and click `Upgrade Plugin` if needed.
- **Repositories**: By default, QGIS connects to the official plugin repository, but you can add custom repositories in the `Settings` tab.
- **Stability**: Be aware of plugin stability ratings; experimental plugins might not work perfectly on all systems.

#### Additional Resources
- For detailed documentation or help with specific plugins, refer to the plugin’s documentation, usually available in the `About` section of each plugin in the Plugin Manager.


## Vector Layers and Atrribute Table
In the next tutorial, we will create a global map by country. Here, we will add a few different data layers to our map project, some which we will ultimately use in our new map and another for comparison, as a means of learning to navigate the interface.  

### Add Vector Layer
#### 1. **Add a Vector Layer**:
You can add a vector layer in several ways. Here are the most common methods:

##### Method 1: Using the 'Data Source Manager'
   - Click on the `Layer` menu at the top.
   - Select `Add Layer` > `Add Vector Layer...` from the dropdown menu.
   - In the `Data Source Manager` window, under the `Source` tab, click the `…` button next to `Vector Dataset(s)`.
   - Navigate to the location of your vector file (e.g., Shapefile, GeoJSON, KML, etc.), select the file, and click `Open`.
   - Click `Add` to load the vector layer into QGIS.

##### Method 2: Drag and Drop
   - Simply drag and drop the vector file from your file explorer directly into the QGIS map canvas. QGIS will automatically add the layer.

##### Method 3: Using the Browser Panel
   - If the `Browser` panel is visible in QGIS (usually on the left side), you can navigate to your data folder directly within this panel.
   - Locate your vector file, right-click on it, and select `Add Layer to Project`.

#### 2. Verify the Layer:
   - After adding the layer, it will appear in the 'Layers' panel on the QGIS interface.
   - You can now view the layer on the map canvas. If the layer does not display as expected, ensure the file format is supported and that the coordinate reference system (CRS) is correct.

#### 3. Set the Coordinate Reference System (CRS):
   - When you add a vector layer, QGIS usually prompts you to confirm the CRS.
   - Ensure the CRS matches your data. You can change it by right-clicking on the layer in the `Layers` panel, selecting `Layer CRS`, and then `Set Layer CRS`.

#### 4. Save the Project:
   - Once your vector layer is added and displayed correctly, save your project by clicking on `Project` > `Save` or `Save As...`.

### Tips:
- Make sure that all required files (e.g., .shp, .shx, .dbf for Shapefiles) are in the same directory.
- Use the `Identify Features` tool to check the attributes of your vector data.
- If you need to style your vector layer, right-click on the layer, select `Properties`, and use the `Symbology` tab.

### Exploring the Attribute Table of a Vector Layer in QGIS

To explore the attributes of a vector layer in QGIS, you can access the *Attribute Table* associated with the layer, which provides detailed information for each feature within the dataset.

#### 1. Accessing the Attribute Table

1. **Right-click** on the layer name in the Layers panel.
2. **Select** `Open Attribute Table` from the context menu.

This action opens the Attribute Table, displaying all the attributes associated with each feature in the layer. For example, in a basic administrative boundary layer, the Attribute Table might contain fields such as country names, regions, subregions, and ISO country codes. These fields can be of different data types, such as text or numeric.

#### 2. Interacting with the Attribute Table

- **Sorting:** Click on a field header to sort the table by that field. This helps organize and analyze the data in a meaningful order.
- **Selecting Features:** Click on a row label (e.g., the number on the left of each row) to select a feature. The corresponding feature will also be highlighted in the map's data frame.
  
In the example below, the table is sorted by the `Name` field. The first feature is selected, highlighting the corresponding polygon in the map.

#### 3. Understanding Attribute Data Types

The Attribute Table may include various fields:
- **Text Fields:** These fields contain string values, such as country names or regional classifications.
- **Numeric Fields:** These fields contain numeric values that can be used in calculations. For example, the `Cnt_Code` field contains numeric ISO country codes.
- **Text-Formatted Numbers:** Some fields, like `ISO_N3`, appear numeric but are stored as text, preventing mathematical operations.

Each field is of a single data type, and it's important to recognize whether data is formatted as text or numeric, as this affects how you can manipulate and analyze the data.

#### 4. Selecting and Deselecting Features

- To **deselect** any selected features, click the `Deselect All` button on the Attribute Table's toolbar, or use the `Deselect All` option from the Attributes Toolbar.
  
![Deselect]

#### 5. Interactive Selection and Inspection

You can also interactively select features using the map view:
- Use the `Selection Tool` from the Attributes Toolbar to select polygons directly on the map. The corresponding rows in the Attribute Table will be highlighted.
- To view only the selected features in the table, choose `Show Selected Features` from the filter drop-down menu.

For instance, if you select Indonesia in the map, the Attribute Table shows that multiple polygons represent Indonesia as a single multipart feature.

![InteractiveSelection]

#### 6. Navigating the Map

While exploring features, you can navigate through the map using the Map Navigation Toolbar:
- **Zoom and Pan:** Use the toolbar tools or your mouse (scroll to zoom, hold the middle button to pan) to adjust the view.
- To reset your view, click the `Zoom Full` button to return to the map's full extents.

![NavigationToolbar]

#### 7. Final Steps

After exploring the features and attributes, remember to:
- **Deselect** any selected features using the `Deselect All` button.
- **Save** your QGIS map project to preserve any changes or selections made during your exploration.

### Raster Layers

A raster in GIS is a grid of cells (pixels), each with a value representing information such as colour, elevation, temperature, or any other variable.
The grid layout of a raster allows it to represent spatial data, similar to a digital photo or image.
The size of each cell (pixel) in a GeoRaster determines the resolution, which is the ground area that each pixel covers. Higher resolution means smaller cells and more detail, while lower resolution means larger cells and less detail.


#### 1. **Add a raster Layer**:
You can add a vector layer in several ways. Here are the most common methods:

##### Method 1: Using the 'Data Source Manager'
   - Click on the `Layer` menu at the top.
   - Select `Add Layer` > `Add Raster Layer...` from the dropdown menu.
   - In the `Data Source Manager` window, under the `source` tab, click the `…` button next to `Raster Dataset(s)`.
   - Navigate to the location of your vector file (e.g., Shapefile, GeoJSON, KML, etc.), select the file, and click `Open`.
   - Click `Add` to load the vector layer into QGIS.

##### Method 2: Drag and Drop
   - Simply drag and drop the raster file from your file explorer directly into the QGIS map canvas. QGIS will automatically add the layer.

##### Method 3: Using the Browser Panel
   - If the `Browser` panel is visible in QGIS (usually on the left side), you can navigate to your data folder directly within this panel.
   - Locate your raster file, right-click on it, and select `Add Layer to Project`.

#### 2. Verify the Layer:
   - After adding the layer, it will appear in the 'Layers' panel on the QGIS interface.
   - You can now view the layer on the map canvas. If the layer does not display as expected, ensure the file format is supported and that the coordinate reference system (CRS) is correct.

## Print Composer

The QGIS Print Layout (now known as "Print Composer" in older versions of QGIS) is a powerful tool for creating high-quality maps and layouts and exporting them.

#### Step 1: Open Print Layout

- Go to the `Project` menu and select `New Print Layout`.
- Give your layout a name in the pop-up window and click `OK`. This opens the Print Composer interface.

#### Step 2: Change Media Size
- In the right-hand panel, click on the `Layout` tab to access the layout settings.
- Under the `Page Properties` section, find the `Size` dropdown menu. This menu allows you to select from standard sizes such as A4, A3, Letter, or other predefined formats.
- To set a custom size:
   - Choose `Custom` from the `Size` dropdown menu.
   - Enter the desired width and height in the `Width` and `Height` fields. Make sure to specify the units (e.g., millimeters, inches) from the units dropdown next to the fields.
5. Adjust the `Orientation` to either `Portrait` or `Landscape` to suit your layout needs.
6. If you have multiple pages, adjust settings for each page by navigating through the pages using the `Current Page` dropdown or by adding new pages with the `Add Page` button.

#### Step 3: Add a Map to the Layout
- In the Print Composer, click on the `Add Map` tool in the toolbar (icon looks like a map).
- Click and drag on the canvas to draw a rectangle where you want your map to appear. The map from your main QGIS window will be displayed here.
- Adjust the map's extent and scale by using the `Item Properties` panel on the right. You can also pan and zoom the map within the frame by enabling the `Move Item Content` tool.

#### Step 4: Add Other Elements
You can add various elements to your layout, such as:

- **Legend:** Click `Add Legend` and place it on your layout. The legend automatically includes all layers from your map, but you can customize it through the `Item Properties`.
- **Scale Bar:** Click `Add Scalebar` and place it on your map. Customize it using the `Item Properties` for style, units, and division settings.
- **North Arrow:** Click `Add North Arrow` and place it on your layout. Choose a style and adjust its position and size in the `Item Properties`.

#### Step 5: Customize Layout
1. **Arrange Elements:** Select and move items around the canvas to organize your layout. Use the `Align` and `Distribute` tools from the toolbar for precise positioning.
2. **Set Layout Size:** In the `Layout` panel, you can set the page size (e.g., A4, Letter) and orientation (portrait or landscape).
3. **Style Elements:** Customize fonts, colors, and borders through the `Item Properties` for each element to make your map look professional.

#### Step 6: Export Your Map
1. Once your layout is complete, you can export it using the `Layout` menu:
   - `Export as Image` (e.g., PNG, JPEG).
   - `Export as PDF` for a print-ready file.
   - `Export as SVG` if you need a vector format for further editing in graphic design software.
2. Choose your export settings, such as resolution and file path, and click `Save`.

#### Tips and Tricks
- **Lock Elements:** Use the lock button in the `Items` panel to prevent accidentally moving or altering elements.
- **Grids and Guides:** Use the grid and guide tools under the `View` menu to align elements precisely.
- **Templates:** Save your layout as a template if you plan to create similar maps in the future. Templates can be reused to maintain consistency in map production.

That's it! You've created a map layout using the QGIS Print Composer. Experiment with different styles and elements to make your maps informative and visually appealing.