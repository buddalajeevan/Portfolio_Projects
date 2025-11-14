# Microsoft Fabric Ecommerce Data Pipeline Project

## Project Overview
This project demonstrates an end-to-end **Data Engineering workflow using Microsoft Fabric**, designed to ingest, transform, and analyze ecommerce source data using the **Lakehouse Medallion Architecture (Bronze, Silver, Gold)**.  
The pipeline includes data ingestion from ADLS, PySpark-based transformations, semantic modeling, and visualization using Power BI—all within Microsoft Fabric.

---

## Data Flow Summary
- Source ecommerce data uploaded to **Azure Data Lake Storage (ADLS)** in **CSV format**.  
- Built an **ETL pipeline in Microsoft Fabric** to load raw data into the **Lakehouse Bronze layer** in **Parquet** format.  
- Performed data cleaning, transformations, and joins using **PySpark notebooks** within Microsoft Fabric and loaded refined data into the **Silver layer**.  
- Applied aggregation logic and business metrics and stored analytics-ready data in the **Gold layer**.  
- Created a **semantic model** in Microsoft Fabric using the Gold layer data.  
- Built interactive **Power BI reports inside Fabric** for ecommerce insights.

---

## Architecture Diagram

                       +-------------------------------+
                       |    Azure Data Lake Storage    |
                       |      (Ecommerce CSV Files)    |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     Microsoft Fabric Data     |
                       |          Factory (ETL)        |
                       |   - Ingestion from ADLS       |
                       |   - Load to Lakehouse         |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     Lakehouse - Bronze Layer  |
                       |   (Raw Data in Parquet Format)|
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     PySpark Notebook in       |
                       |      Microsoft Fabric         |
                       |   - Cleaning                  |
                       |   - Transformations           |
                       |   - Joins                     |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     Lakehouse - Silver Layer  |
                       | (Refined, Joined, Standardized)|
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     PySpark Notebook          |
                       |   - Aggregations              |
                       |   - Business Metrics          |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |      Lakehouse - Gold Layer   |
                       |   (Analytics-Ready Data)      |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     Semantic Model (Fabric)   |
                       |   - Measures                  |
                       |   - Relationships             |
                       +---------------+---------------+
                                       |
                                       v
                       +-------------------------------+
                       |     Power BI Reports          |
                       |   - Sales Metrics             |
                       |   - Customer Insights         |
                       |   - Ecommerce Analysis        |
                       +-------------------------------+




---

## Key Components

### Microsoft Fabric Data Factory
- Built an ingestion pipeline to load ecommerce CSV files from ADLS.  
- Stored raw ingested data in **Bronze layer** in Parquet format.

### PySpark Notebooks in Microsoft Fabric
- Cleaned and transformed the raw data.  
- Performed joins between multiple ecommerce tables.  
- Loaded processed data into the **Silver layer**.  
- Applied aggregations (sales metrics, customer insights) and moved results to **Gold layer**.

### Lakehouse Structure
- Created a dedicated **Microsoft Fabric Workspace**.  
- Built a **Lakehouse** containing all three layers:
  - Bronze  
  - Silver  
  - Gold  

### Semantic Model
- Built a **semantic model** using Gold layer data to support BI reporting.

### Power BI Visualization
- Designed Power BI reports **within Fabric** for:
  - Sales performance  
  - Customer order trends  
  - Product-level insights  

---

## Technologies Used
- Microsoft Fabric  
- Fabric Data Factory  
- Fabric Lakehouse  
- PySpark Notebooks  
- Power BI (Fabric integrated)  
- ADLS (Azure Data Lake Storage)  
- CSV / Parquet data formats  
- Medallion Architecture (Bronze, Silver, Gold)

---

## Outcome
Delivered a fully integrated **Microsoft Fabric-based data pipeline** that transforms raw ecommerce data into structured, analytics-ready datasets.  
The project demonstrates a unified workflow—ETL, Lakehouse architecture, semantic modeling, and BI—within a single Fabric environment.


