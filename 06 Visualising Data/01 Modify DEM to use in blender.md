In this tutorial, I'll guide you through using the **Rescale Raster** processing tool in **QGIS** and then saving the output as a **16-bit unsigned TIFF** using the **Warp (Reproject)** tool. Rescaling raster data is commonly used to adjust pixel values to a specific range, which can be essential for image normalization, visualization, and other types of analysis.

### Step 1: Rescaling a Raster in QGIS

1. **Open QGIS and Load Raster Data**
   - Start QGIS and load the raster file you want to process. You can add a raster by clicking **Layer > Add Layer > Add Raster Layer** or by dragging and dropping the raster file into the QGIS interface.

2. **Access the Rescale Raster Tool**
   - Go to the **Processing Toolbox**. If it's not visible, enable it by going to **View > Panels > Processing Toolbox**.
   - In the toolbox, search for **Rescale Raster**. This tool is found under **Raster analysis** or by typing "Rescale Raster" in the search bar.

3. **Set Parameters in the Rescale Raster Tool**
   - Open the **Rescale Raster** tool by double-clicking it.
   - Configure the following parameters:
     - **Input layer**: Select the raster you loaded.
     - **Output min**: Set the minimum value for the output range (`0`).
     - **Output max**: Set the maximum value for the output range (`60000`).
   - Leave other settings at default unless you have specific requirements.
   - **Output file**: Specify an output location or leave it as a temporary file (you’ll save it in the next steps anyway).

4. **Run the Rescale Raster Tool**
   - Click **Run** to execute the tool. The rescaled raster will appear in the Layers panel upon completion.

### Step 2: Saving the Raster as a 16-bit Unsigned TIFF

After rescaling, we can now convert the raster to a **16-bit unsigned TIFF** format using the **Translate (Convert format)** tool.

1. **Open the Translate (Convert format) Tool:**
   - In the **Processing Toolbox**, search for "Translate (Convert format)" to locate the **Translate (Convert format)** tool. Click on it to open the dialog.

2. **Set up the Translate Parameters:**
   - In the **Translate (Convert format)** dialog, configure the following options:
     - **Input layer**: Select the rescaled raster layer created in the previous step.
     - **Output data type** (found under "Advanced Parameters"): Choose **UInt16** (Unsigned Integer 16 bit) from the dropdown menu. This ensures that the output TIFF will be saved as a 16-bit unsigned integer.
   - **Output file**: Specify the location and name for the output file, making sure it has a `.tif` extension to save it as a TIFF.

3. **Run the Translate Tool:**
   - Click **Run** to convert and save the rescaled raster as a 16-bit unsigned TIFF file.
   - After completion, the new file should appear in your **Layers** panel and will also be saved to the specified directory.