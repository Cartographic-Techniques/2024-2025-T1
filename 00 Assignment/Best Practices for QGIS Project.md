# Best Practices for Organizing a QGIS Project

A well-organized QGIS project makes analysis and visualization easier, and ensures reproducibility. Below is a series of best practices and recommended protocols to keep your QGIS project ordered:


## **1. Project Setup**
### 1.1 **Folder Structure**
Organize your files in a clear and consistent directory structure:

- Create a main project folder, e.g., `Project_Name`.
  - **Data:** For raw spatial datasets (e.g., shapefiles, GeoTIFFs).
  - **Outputs:** For analysis results, including exported maps and reports.
  - **Scripts:** For Python scripts, models, or custom functions.
  - **Styles:** For saved QGIS layer styles (.qml) or symbology.
  - **Documentation:** For project notes, metadata, and external documentation.
  - **Backups:** For copies of essential files (consider versioning).
  
### 1.2 **Consistent Naming Conventions**
- Use **meaningful**, concise names (avoid spaces and special characters, prefer underscores).
  - Example: `landuse_2024.shp`, `population_density.geojson`, `rivers_wgs84.shp`
- Use lowercase for file and layer names to maintain consistency.

## **2. Layer Management**
### 2.1 **Layer Grouping**
- Group layers logically by theme, type, or data source. For example:
  - **Basemaps:** Contains raster or vector background layers like OpenStreetMap or satellite imagery.
  - **Data Layers:** Organized by analysis categories (e.g., infrastructure, vegetation, hydrology).
  - **Analysis Results:** Separate group for derived layers or processed outputs.
  - **Temporary/Working Layers:** For intermediate layers that might not be saved long-term.

### 2.2 **Layer Naming**
- Rename layers in the **Layers Panel** to something descriptive and standardized.
  - Example: `roads_main_city`, `elevation_2023`, `population_density_urban_area`.
- Include versioning or dates where relevant for datasets that may change over time.

### 2.3 **Symbology and Styling**
- Save custom styles using **QML files** to maintain consistency across different sessions.
  - Save styles to the project folder (`/Styles`) and reload them if the layer is updated.

## **3. Coordinate Reference Systems (CRS)**
### 3.1 **Set Project CRS**
- Set the project CRS based on your primary dataset or analysis region (e.g., EPSG:4326 for WGS 84 or a local projection).
- Ensure all layers are properly projected on the fly or reprojected to the correct CRS to avoid alignment issues.
- Use **‘Reproject Layer’** from the processing toolbox if you need to permanently reproject a layer.

## **4. Data Integrity and Metadata**
### 4.1 **Metadata Management**
- Ensure that each dataset has metadata, documenting the source, CRS, processing steps, and any assumptions made.
- For large projects, maintain a project metadata file describing all datasets used and analysis steps taken.

## **5. Project File Organization**
### 5.1 **Use Relative Paths**
- In **Project Properties**, ensure **relative paths** are enabled (`Project > Properties > General > Save paths > Relative`).
  - This allows your project to be portable across different machines or folder structures.

### 5.2 **Keep a Clean Map Canvas**
- Avoid cluttering the map canvas with too many visible layers, it will slow your computer performance. Only display layers relevant to the current analysis or task.
- Hide unnecessary layers in the **Layers Panel** (or temporarily move them to an unused group).

## **6. Version Control and Backups**
### 6.1 **Save Project Versions**
- Save different versions of your QGIS project files, especially before significant changes, using a versioning system:
  - Example: `project_v1.qgz`, `project_v2_analysis.qgz`.

### 6.2 **Use External Version Control (Optional)**
- For more complex projects, consider using Git or other version control systems to track changes in scripts, documentation, and possibly even project files.

## **7. Automation and Documentation**
### 7.1 **Automate Tasks with Models and Scripts**
- Use **QGIS Processing Models** or **Python Scripts** to automate repetitive tasks or complex workflows.
- Save your models and scripts in the **/Scripts** folder and clearly document what they do.

### 7.2 **Document Workflow**
- Keep a **log file** or project notes to document:
  - Key steps taken in the analysis.
  - Key decisions or parameters used (e.g., buffer distance, reclassification thresholds).
  - Issues encountered and how they were resolved.

## **8. Dataset Citation Tracking with Zotero (optional)**
Zotero is free and open-source reference management software to manage bibliographic data and related research materials, such as PDF and ePUB files.

Using a tool like Zotero helps efficiently manage dataset citations, while DOIs (Digital Object Identifiers) allow automatic imports and proper citation formatting.

### 3.1 **Set Up Zotero for Dataset Management**
- Install **Zotero** and the relevant **browser extension** (if necessary) to easily capture dataset citations from online repositories.
- Create a new **Zotero Collection** for your project, named after the project (e.g., `Project_Name`), where you will store all dataset citations.

### 3.2 **Using DOIs to Import Dataset Citations Automatically**
- Many spatial datasets, especially from scientific sources and repositories (e.g., Zenodo, Dryad, OpenStreetMap), provide DOIs.
  - To add a dataset to Zotero, click **“Add Item by Identifier”** and paste the dataset’s DOI. Zotero will automatically import citation details like title, author(s), publisher, date, and URL.
  - Example: If using a dataset from a repository that provides a DOI (e.g., `doi:10.1234/example-dataset`), this can be quickly imported, ensuring proper citation and metadata retention.

---

### Example of a Structured QGIS Project Folder:
```
Project_Name/
│
├── Data/
│   ├── roads/
│   │   ├── roads.shp
│   │   ├── roads.dbf
│   │   ├── roads.cpg
│   │   ├── roads.prj
│   │   └── roads.shx
│   │
│   ├── rivers.geojson
│   └── population_density.tif
│
├── Outputs/
│   ├── landuse_analysis_results.shp
│   ├── flood_risk_map.tiff
│   └── final_map_export.pdf
│
├── Scripts/
│   ├── calculate_area.py
│   └── processing_model.model3
│
├── Styles/
│   ├── roads_style.qml
│   ├── water_style.qml
│   └── population_style.qml
│
├── Documentation/
│   ├── metadata.txt
│   └── analysis_notes.md
│
├── Backups/
│   └── project_backup_v1.qgz
│
└── project_name.qgz
```
