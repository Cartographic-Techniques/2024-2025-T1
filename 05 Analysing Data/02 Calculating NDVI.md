### Tutorial: Calculating NDVI in QGIS

---

#### **What is NDVI?**

**Normalized Difference Vegetation Index (NDVI)** is a numerical indicator that uses the red and near-infrared bands of the electromagnetic spectrum to analyze vegetation health. It's one of the most widely used vegetation indices because it effectively measures and monitors vegetation growth, density, and health. NDVI values range from -1 to +1, where:

- **Values near +1** indicate dense green vegetation (high vegetation health).
- **Values around 0** suggest bare soil or sparse vegetation.
- **Values near -1** are typically associated with water, urban areas, or other non-vegetated surfaces.

#### **What is NDVI used for?**

NDVI is an essential tool for environmental scientists, ecologists, and agricultural analysts because it helps:

1. **Monitor Crop Health**: Farmers use NDVI to assess the health of crops over growing seasons.
2. **Track Deforestation**: NDVI can detect areas of forest degradation or deforestation.
3. **Analyze Drought Impact**: NDVI values help assess vegetation stress during droughts.
4. **Urban Planning**: It helps determine green spaces and vegetation coverage in urban environments.

#### **The Math Behind NDVI**

NDVI is calculated using the following formula:

`NDVI = (NIR - Red)/(NIR + Red)`

Where:

- **NIR** = Reflectance in the Near-Infrared Band
- **Red** = Reflectance in the Red Band

Healthy vegetation absorbs most visible light and reflects a significant amount of near-infrared light. In contrast, stressed or sparse vegetation reflects more visible light and less near-infrared light. This contrast enables NDVI to quantify vegetation health.

---

### **Step-by-Step Guide to Calculate NDVI in QGIS**

To calculate NDVI in QGIS, you need a multispectral image (usually from satellite imagery) containing at least the Red and Near-Infrared (NIR) bands.

#### **Step 1: Load the Satellite Image**

1. Open QGIS.
2. Go to **Layer > Add Layer > Add Raster Layer**.
3. Select and load your multispectral image (e.g., a .tif file from Sentinel-2 or Landsat).

Ensure you have a satellite image with separate Red and NIR bands. Landsat-8 and Sentinel-2, for example, provide this data:
   - For **Landsat 8**: Band 4 is Red, Band 5 is NIR.
   - For **Sentinel-2**: Band 4 is Red, Band 8 is NIR.

#### **Step 2: Open the Raster Calculator**

1. Go to **Raster > Raster Calculator** in the top menu.
2. The **Raster Calculator** window will open, where you’ll enter the NDVI formula.

#### **Step 3: Enter the NDVI Formula**

1. In the **Raster Calculator**, identify your Red and NIR bands. They will appear in the "Raster bands" panel and may look something like `image_band4@1` for Red and `image_band5@1` for NIR.
2. Enter the NDVI formula in the expression field as follows:

   ```plaintext
   ( "image_band5@1" - "image_band4@1" ) / ( "image_band5@1" + "image_band4@1" )
   ```

   Replace `"image_band5@1"` and `"image_band4@1"` with the correct band names from your image.

3. In **Output layer**, specify the path and filename for the NDVI output.

4. Click **OK** to run the calculation. QGIS will process the formula and generate a new raster layer representing NDVI values.

#### **Step 4: Visualize the NDVI Output**

1. Once the NDVI raster layer is created, you can adjust its color ramp to better visualize the data.
   - Right-click on the NDVI layer and go to **Properties > Symbology**.
   - Choose **Singleband pseudocolor** and select a color ramp that highlights vegetation health (e.g., green for high values and red for low values).
2. Click **Apply** and then **OK** to see your NDVI map.

#### **Step 5: Analyze and Interpret**

Now that the NDVI layer is created and styled, you can use it for various analyses. High NDVI values (close to +1) represent dense, healthy vegetation, while lower values indicate sparse or stressed vegetation.

---

### **Additional Tips**

- **Save and Export**: Save your NDVI layer as a new file if you want to use it outside of QGIS by right-clicking on it and selecting **Export > Save As**.
- **Thresholding**: To isolate areas with specific NDVI ranges (e.g., areas with high vegetation), you can use the **Raster Calculator** to create a conditional expression (e.g., NDVI > 0.6).

---

By following these steps, you can efficiently calculate and analyze NDVI in QGIS, providing valuable insights into vegetation health for various applications.