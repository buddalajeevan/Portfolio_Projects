End-to-End Retail Data Engineering Project using Azure Medallion Architecture

As a Data Engineer skilled in Azure, Databricks, and Power BI, I’m passionate about designing scalable data pipelines that transform raw data into actionable business insights. This project showcases my ability to integrate multiple Azure services and apply the Medallion Architecture to deliver an end-to-end analytics solution.

Project Overview:
Built a comprehensive retail data engineering pipeline to process and analyze data from multiple sources, including stores, products, customers, and transactions. The objective was to automate data ingestion, transformation, and visualization for better decision-making in retail operations.

Key Steps & Implementation:

Data Ingestion:

Extracted customer data from a REST API (JSON format) using Azure Data Factory (ADF).

Created an Azure SQL Server and Azure SQL Database, and inserted store, product, and transaction data into structured tables using SQL.

Built ADF ETL pipelines to load all raw data into Azure Data Lake Storage Gen2 (ADLS) in Parquet format under the Bronze layer.

Data Transformation & Processing:

Mounted ADLS Gen2 in Azure Databricks and used PySpark to read, clean, and transform all four datasets.

Performed data cleansing, standardization, and joins to unify the data model in the Silver layer.

Applied aggregations and business logic to produce the Gold layer, ready for analytics and reporting.

Data Visualization & Insights:

Exported aggregated Gold layer data from Databricks as CSV files.

Connected the curated data to Power BI and designed interactive dashboards to visualize sales performance, customer segmentation, and store-level trends.

Architecture:
🔹 Bronze Layer: Raw data from API & SQL (stored in Parquet)
🔹 Silver Layer: Cleaned, standardized, and joined data
🔹 Gold Layer: Aggregated, analytics-ready data

Tools & Technologies:
Azure Data Factory | Azure Databricks (PySpark) | Azure SQL Database | Azure Data Lake Storage Gen2 | Power BI | REST API | JSON | SQL | Medallion Architecture

Outcome:
Delivered a fully automated, scalable data pipeline that streamlined the flow of data from ingestion to analytics, enhancing reporting efficiency and enabling data-driven insights for retail operations.
