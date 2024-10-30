Calculating vegetation loss from wildfires using two Landsat 8 images in QGIS

#### 1. Load the Images

- **Open QGIS**.
- **Add Raster Layers**: 
  - Go to **Layer** > **Add Layer** > **Add Raster Layer**.
  - Browse to select the two Landsat 8 images (pre-fire and post-fire).
  
#### 2. Calculate NDVI (Normalized Difference Vegetation Index) for Both Images

NDVI is a common way to assess vegetation health.
Look at "02 Calculating NDVI" for detailed instructions on how to calculate NDVI. 

#### 3. Calculate Vegetation Loss

To calculate vegetation loss, you can subtract the post-fire NDVI from the pre-fire NDVI:

- Open the **Raster Calculator** again.
- Input:
  ```
  "NDVI_PreFire" - "NDVI_PostFire"
  ```
- Save this output as `Vegetation_Loss`.


#### 4. Analyze the Results
The result of this calculation is a new raster layer where each pixel represents the change in NDVI due to the fire.

- **NDVI Change Analysis**: By subtracting the **post-fire NDVI** from the **pre-fire NDVI**:
  - We get a **positive value** if the NDVI has decreased after the fire (indicating vegetation loss).
  - We get a **value close to 0** if there’s little or no change (indicating stable or unaffected areas).
  - We might even get **negative values** if vegetation has somehow increased, though this is uncommon right after a wildfire.

##### Interpreting the Vegetation Loss Values:

- **High Positive Values**: Large positive values indicate a significant drop in NDVI, which corresponds to higher vegetation loss. For instance, if `NDVI PreFire = 0.7` and `NDVI PostFire = 0.1`, then: `Vegetation Loss: 0.7 - 0.1 = 0.6`.
  This is a high loss, implying that dense vegetation before the fire was largely destroyed.

- **Low Positive Values**: Smaller positive values indicate minor vegetation loss. For example, `NDVI PreFire = 0.4` and `NDVI PostFire = 0.3` yield:
`  Vegetation Loss: 0.4 - 0.3 = 0.1`. This suggests a slight reduction in vegetation, possibly in areas where the fire had a limited effect.

- **Values Close to Zero**: When the value is close to zero, it means there was little to no change in NDVI, implying that vegetation cover was likely unaffected by the fire.

- **Negative Values**: If you get negative values, they might indicate post-fire vegetation growth (such as new grass in a previously barren area) or could be due to factors unrelated to the fire, like seasonal changes or soil exposure differences.


- **Classify the Vegetation Loss**: You might want to classify the loss into different categories (e.g., high loss, moderate loss, low loss) by using symbology to visualize the loss areas effectively. You can create a color ramp to represent different levels of loss.

#### 5. Area Calculation (Optional)

If you want to calculate the area of vegetation loss:

- Convert the raster loss layer to a vector layer using **Raster** > **Conversion** > **Polygonize (Raster to Vector)**.
- Use the **Field Calculator** to add a new field calculating area (in square meters or hectares) for each polygon.
