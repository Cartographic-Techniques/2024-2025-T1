## Google Earth Engine Tutorial

This tutorial will guide you through using Google Earth Engine to work with datasets, explore metadata, use sample code, upload and import shapefiles, clip images, and download them to Google Drive.

### 1. Open a Dataset from the Earth Engine Website

1. **Go to the Earth Engine Dataset Page:**
   - Visit the [Google Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/).

2. **Select a Dataset:**
   - Browse or search for a dataset of interest (e.g., `Landsat 8 Surface Reflectance`).

3. **Open the Dataset:**
   - Click on the dataset name to open its description page. This page provides detailed information about the dataset.

### 2. Explore Metadata/Description

1. **View Metadata:**
   - On the dataset description page, you can see the dataset’s metadata, such as `provider`, `resolution`, `bands`, `temporal coverage`, and `image properties`.

2. **Understand Dataset Properties:**
   - Take note of important properties like `band names`, `resolution`, and `scale` that will be useful when analyzing and processing the data in Earth Engine.

### 3. Copy "Explore with Earth Engine" Example Code

1. **Find Example Code:**
   - On the bottom of the dataset description page, look for the “Explore with Earth Engine” section.

2. **Copy the Code:**
   - Click on the "Run in Earth Engine" button to open the example code in the Earth Engine Code Editor, or simply copy the provided JavaScript code.

3. **Paste in Code Editor:**
   - Go to the [Google Earth Engine Code Editor](https://code.earthengine.google.com/) and paste the copied code into the editor.

### 4. Upload a Shapefile to the Assets

1. **Prepare the Shapefile:**
   - Ensure your shapefile is in a `.zip` format containing all necessary components (`.shp`, `.shx`, `.dbf`, etc.).

2. **Upload the Shapefile:**
   - In the Code Editor, click on the “Assets” tab.
   - Click on the “+ New” button and select “Table upload”.
   - Choose your `.zip` file and upload it.
   - Once uploaded, the shapefile will appear under your assets.

### 5. Import the Shapefile in the Code

1. **Add Shapefile to Code:**
   - In the Code Editor, under the “Assets” tab, click your shapefile and select “Import”.
   - This will add an import statement at the top of your script, like:
     ```javascript
     var tabe = ee.FeatureCollection("users/your_username/shapefile_name");
     ```

### 6. Clip Image to Shapefile's Extent

1. **Clip the Image:**
   - Clip the image using the shapefile:
     ```javascript
     var clipped_image = imageToBeClipped.clip(shapefile);
     ```
	- Modify `imageToBeClipped` with the actual name of the image you want to clip. The name of the image can vay from a dataset example to another.
	- If you are working with an image collection, be sure to convert the collection into a single image with `.mean()`
	

2. **Visualize:**
   - Modify the `Map.addLayer` statement including the clipped image:
	- Use `Map.centerObject(shapefile);` to center the map to the extent of your shapefile.
	 
### 7. Download Image to Google Drive

1. **Export the Image:**
   - Use the `Export` function to save the image to Google Drive:
     ```javascript
     Export.image.toDrive({
       image: clipped_image,
       description: 'clipped_image_export',
       folder: 'EarthEngineExports',
       scale: 30,
       region: shapefile.geometry().bounds(),
       maxPixels: 1e9
     });
     ```

2. **Run the Export:**
   - Click the “Run” button in the Tasks tab on the right side of the Code Editor.
   - You can monitor the export status in the Tasks tab.

3. **Check Google Drive:**
   - Once the task completes, go to your Google Drive in the specified folder to find the exported image.

Google Earth Engine (GEE) hosts a vast collection of datasets across various themes, including climate, land cover, vegetation, hydrology, and socioeconomics. Here are some interesting datasets you can explore:

## Google Earth Engine Datasets to Get Started

### 1. **Landsat Collections**
   - **USGS Landsat 8**: [Link](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2)
   - **USGS Landsat 7**: [Link](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2)
   - These datasets provide multispectral images useful for land cover analysis, vegetation studies, and monitoring changes over time.

### 2. **Sentinel-2**
   - **Sentinel-2 MSI: MultiSpectral Instrument, Level-1C**: [Link](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED)
   - Offers high-resolution (10-60m) optical imagery for land monitoring, agriculture, forestry, and environmental studies.

### 3. **MODIS (Moderate Resolution Imaging Spectroradiometer)**
   - **MODIS Land Surface Temperature & Emissivity (MOD11A1)**: [Link](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A1)
   - **MODIS Vegetation Indices (NDVI/EVI)**: [Link](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD13A1)
   - Useful for temperature monitoring, vegetation health, and phenology studies.

### 4. **Global Land Cover**
   - **Global Land Cover (GLC30) 2010**: [Link](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v100#description)
   - High-resolution global land cover maps with 10m resolution, providing detailed land cover classification.

### 5. **Elevation Data**
   - **SRTM Digital Elevation Data**: [Link](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4)
   - Provides global elevation data at 90m resolution, useful for topography and watershed analysis.

### 6. **Climate Data**
   - **ERA5 Climate Reanalysis**: [Link](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_MONTHLY)
   - Provides a comprehensive set of atmospheric variables at a high temporal resolution.

### 7. **Precipitation and Hydrology**
   - **CHIRPS Daily: Climate Hazards Group InfraRed Precipitation with Station data**: [Link](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_DAILY)
   - **Global Surface Water**: [Link](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_2_GlobalSurfaceWater)
   - Useful for hydrological modeling, drought monitoring, and water resource management.

### 8. **Socioeconomic Data**
   - **Global Human Settlement Population Grid (GHS-POP)**: [Link](https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2016_POP_GPW_GLOBE_V1)
   - Provides population density and distribution, useful for urban planning and socio-economic studies.

### 9. **Vegetation and Forest Monitoring**
   - **Global Forest Change (2000-2023)**: [Link](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11)
   - Useful for tracking deforestation, forest health, and ecosystem studies.

### 10. **Air Quality and Atmospheric Data**
   - **Sentinel-5P (TROPOMI) Air Quality Data**: [Link](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2)
   - Monitors air pollutants like NO2, CO, and aerosols, critical for environmental and health assessments.