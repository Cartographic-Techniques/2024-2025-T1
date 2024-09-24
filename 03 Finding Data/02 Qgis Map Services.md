This tutorial covers the basic steps to add and interact with WMS, WMTS, and WCS services in QGIS. Each type of service allows for different kinds of interaction with geospatial data. For advanced usage, such as scripting or automated queries, you can explore QGIS’s Python API or plugins that enhance service handling capabilities.

- **WMS** provides map images rendered by the server.
- **WMTS** provides tiled map images for faster rendering.
- **WCS** provides raster data, such as satellite imagery or terrain models.

### Prerequisites
2. **Service URLs**: You should have URLs for the WMS, WMTS, and WCS services you want to use.

### 1. Adding a WMS Layer

1. **Open QGIS** and go to the *Layer* menu.
2. Select **Add Layer** > **Add WMS/WMTS Layer**.
   
3. Click on the **New** button to create a new WMS connection.
   - **Name**: Give your connection a descriptive name.
   - **URL**: Paste the WMS URL provided by the service.
   - Optional fields:
     - **Username/Password**: If the service requires authentication.
     - **Ignore GetMap URI reported by the server**: For resolving URL issues.
   
4. Click **OK** to save the connection, then select the connection from the list and click **Connect**.
5. You will see a list of available layers. Choose the layers you want to add and click **Add**.
6. The selected layers will be added to your QGIS project.

### 2. Adding a WMTS Layer

1. Go to the *Layer* menu and select **Add Layer** > **Add WMS/WMTS Layer**.
2. Click **New** to create a new connection, just like in the WMS example.
   - **Name**: Provide a name for your WMTS connection.
   - **URL**: Enter the WMTS service URL.
3. Click **OK** and then **Connect**.
4. Select the WMTS layers you want to add from the list and click **Add**.
5. The WMTS layers will appear in your project as a tiled map.

### 3. Adding a WCS Layer

1. Go to the *Layer* menu and select **Add Layer** > **Add WCS Layer**.
   
2. Click on the **New** button to create a new WCS connection.
   - **Name**: Enter a name for the connection.
   - **URL**: Paste the WCS service URL.
   - Optional fields:
     - **Username/Password**: If required for authentication.
     - **Ignore GetCoverage URI reported by the server**: For URL issues.
   
3. Click **OK** to save the connection, then select it from the list and click **Connect**.
4. A list of available coverages (datasets) will appear. Choose the one you need and click **Add**.
5. The selected coverage will be added as a raster layer in your project.

### 4. Styling and Visualizing Layers

1. Once added, you can change the symbology of WMS and WCS layers like any other QGIS layer.
2. Right-click on the layer in the *Layers Panel* and select **Properties**.
3. For WMS/WMTS, you can choose different styles provided by the service.
4. For WCS, you can adjust the band rendering, apply colormaps, and modify contrast settings.

### 5. Troubleshooting

- **Connection Issues**: Ensure that the URL is correct and accessible. Sometimes, firewalls or internet restrictions can block access.
- **Layer Not Displaying**: Check the Coordinate Reference System (CRS). QGIS automatically reprojects layers, but it’s good to match the project CRS with the service CRS.
- **Authentication Required**: Some services need a username and password. Ensure you have the correct credentials.

### 6. Saving and Sharing the Project

1. Save your project by going to **Project** > **Save As...** and choose a location and filename.
2. To share the project, you can save it as a .qgz file and include any local data sources. For web services, your collaborators will need access to the same WMS, WMTS, or WCS URLs.


Here are some publicly available examples for each type of service (WMS, WMTS, and WCS) that you can use to practice in QGIS:

### 7. WMS (Web Map Service)
WMS services provide rendered map images that you can overlay on your project. Here are some popular WMS services:

- **NASA Global Imagery Browse Services (GIBS)**
  - URL: `https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi`
  - Description: Provides daily satellite imagery, such as MODIS Terra and Aqua.

- **European Space Agency (ESA) WorldCover**
  - URL: `https://esa-worldcover.org/en`
  - WMS URL: `https://services.terrascope.be/wms/v2https://services.terrascope.be/wms/v2`
  - Description: ESA WorldCover 10m resolution land cover map.

### 8. WMTS (Web Map Tile Service)
WMTS provides map data in the form of pre-rendered tiles, which makes it efficient for web mapping and fast rendering.

- **ESRI National Geographic Basemap**
  - URL: `https://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/WMTS`
  - Description: A high-quality basemap suitable for general-purpose maps.

- **NASA GIBS WMTS (Global Imagery Browse Services)**
  - URL: `https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi`
  - Description: Provides various layers, including MODIS true color and snow cover.

### 9. WCS (Web Coverage Service)
WCS provides access to raster data, such as elevation models or satellite imagery, and allows you to download data in different formats.

- **USGS National Elevation Dataset (NED)**
  - URL: `https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WCSServer`
  - Description: Provides elevation data for the United States.

- **Copernicus Land Monitoring Service (CLMS)**
  - URL: `https://land.copernicus.vgt.vito.be/PDF/datapool/wcs?`
  - Description: Offers access to satellite data and derived products, such as vegetation indices.

- **NASA SEDAC Global Population Data**
  - URL: `https://sedac.ciesin.columbia.edu/geoserver/wcs`
  - Description: Provides gridded population data and other demographic datasets.

These services provide a wide range of geospatial data for various applications, such as mapping, analysis, and research in QGIS.