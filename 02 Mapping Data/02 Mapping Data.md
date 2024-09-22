#2. Mapping Data

## Working with Projections

###On-the-Fly CRS Transformation
On-the-Fly CRS Transformation allows you to display layers with different coordinate reference systems (CRS) in the same project, without permanently changing the data.


#### 1 **Add a Layer**:
   - Go to `Layer` > `Add Layer`
   - Select your spatial data files (shapefiles, GeoJSON, raster etc.) and load them into the project.

#### 2 **Set Project CRS**
   - Go to the bottom-right of the QGIS window, where the CRS of the project is displayed (e.g., `EPSG:4326`).
   - Click on the CRS to open the `Project Properties` window.
   - Click on the `filter` tab and either search for a specific CRS (like `EPSG:4326` for WGS 84) or pick from the list.
   - Click `OK` to apply the changes.

###Reprojecting a Layer
Reprojecting a layer means permanently changing its CRS and saving the transformed coordinates to a new file.

QGIS provides a convenient tool for reprojecting a layer via the **Processing Toolbox**, which offers a quick and efficient way to change a layer's CRS.

#### 1. **Open the Processing Toolbox**:
   - Go to the `Processing` menu and click `Toolbox` to open the Processing Toolbox.

#### 2. **Search for the "Reproject Layer" Tool**:
   - In the `Processing Toolbox`, type "*Reproject layer*" in the search bar.
   - Double-click `Reproject layer` to open the tool dialog.

#### 3. **Set Input Parameters**:
   - In the `Reproject layer` dialog, you’ll need to specify the following:
     - `Input Layer`: Select the layer you want to reproject from the dropdown list.
     - `Target CRS`: Click the CRS selector button next to this field to choose the new CRS for the layer. You can search for the desired CRS (e.g., `EPSG:3857` (WGS 84 / Pseudo Mercator) or `EPSG:32633` (UTM Zone 33N) or select from the list.
   
#### 4. **Choose Output File**:
   - Click the `…` button next to `Reprojected` to specify where to save the new reprojected layer. You can save it as a new file (e.g., a shapefile, GeoJSON, or another format).

#### 5. **Run the Tool**:
   - After selecting the input layer, target CRS, and output file location, click `Run` to perform the reprojection.
   - The tool will reproject the layer and save it as a new file with the new CRS.

#### 6. **Check the Reprojected Layer**:
   - Once the process is complete, the reprojected layer will be added to the `Layers Panel`.
   - You can right-click the layer, go to `Layer Properties`, and check the `Information` tab to confirm that the new CRS has been applied.

This method is efficient and allows you to quickly reproject layers while working within the QGIS interface.


### Creating a Custom Projection

Now, we will create a custom projection using an Orthographic projection as the base. The Orthographic projection shows the Earth as a globe from a specific point, but it’s not commonly used for spatial analysis because it's only accurate near the center of projection. However, it's useful for visualizing the globe in a perspective similar to the one of satellites.

#### 1. **Open the Custom CRS Dialog**:
   - Go to `Settings` > `Custom Projections…`.
   - In the dialog that opens, you’ll see a list of existing custom projections (if any). Click `+` to add a new CRS.

#### 2. **Define the Custom CRS**:
   - **Name your custom CRS**: For example, “Custom Orthographic Projection”.
   - In the `Parameters` box, you will define your custom projection using `Proj4` syntax, which is used by QGIS to define CRS parameters.
   
   A Proj4 string for an **orthographic projection** centered at 0° longitude and 0° latitude would look like this:
   
   ```
   +proj=ortho +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs
   ```

   This is what each parameter means:
   - `+proj=ortho`: Specifies the **orthographic projection**.
   - `+lat_0=0`: The **latitude of origin** (the center of the projection) at 0°.
   - `+lon_0=0`: The **longitude of origin** at 0°.
   - `+x_0=0` and `+y_0=0`: The false easting and northing (shifts the projection center, but here they’re set to 0).
   - `+datum=WGS84`: The datum used for the projection (WGS 84).
   - `+units=m`: The units for the projection (meters).
   - `+no_defs`: Ensures no additional default parameters are used.

#### 3. **Modifying the Projection**:
   - If you want to center the projection on a different location (e.g., Amsterdam), you would change the latitude and longitude parameters. For example:
     ```
     +proj=ortho +lat_0=52.377956 +lon_0=4.897070 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs
     ```
   - This would create an orthographic projection centered on Amsterdam.

#### 4. **Test the Projection**:
   - After entering the Proj4 string, click **OK** to save your custom projection.
   - You can now apply this projection to layers in your project.
   - To test it, go to `**Project**` > `**Properties**` > `**CRS**` and search for the name of your custom projection.
   - Apply the projection to the project, and your map will be displayed using the orthographic projection.

#### 5. **Applying the Custom CRS to a Layer**:
   - To apply your custom CRS to a specific layer (not the whole project), you can follow the **reprojection** steps mentioned earlier but select your custom projection from the CRS dropdown menu.