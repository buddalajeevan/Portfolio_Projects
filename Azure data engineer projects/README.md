# Azure Retail Data Pipeline Project

## Project Overview

This project demonstrates an end-to-end **Data Engineering solution** using **Azure Data Factory**, **Azure Databricks**, and **Power BI**, designed to process and analyze retail data from multiple sources using the **Medallion Architecture** (Bronze, Silver, Gold layers). The objective is to integrate and transform raw data into meaningful insights for retail performance analysis.

## About Me

I am **Buddala Pavan Jeevan**, a Data Engineer with hands-on experience in building and orchestrating data pipelines using Azure cloud technologies. My expertise includes Azure Data Factory, Databricks (PySpark), and Power BI for designing scalable data solutions and interactive dashboards.

---

## Architecture Diagram

```
                +--------------------------+
                |    Data Sources          |
                |--------------------------|
                | 1. Azure SQL Database    |
                | 2. API (JSON - Customers)|
                +-------------+------------+
                              |
                              v
                    +---------+---------+
                    | Azure Data Factory |
                    | (Data Ingestion)   |
                    +---------+---------+
                              |
                              v
                  +-----------+------------+
                  | ADLS Gen2 - Bronze Layer |
                  | (Raw Data - Parquet)     |
                  +-----------+------------+
                              |
                              v
                    +---------+---------+
                    | Azure Databricks   |
                    | (Data Cleaning,    |
                    |  Joining, &        |
                    |  Transformations)  |
                    +---------+---------+
                              |
                              v
                  +-----------+-----------+
                  | ADLS Gen2 - Silver Layer |
                  | (Cleaned, Joined Data)   |
                  +-----------+-----------+
                              |
                              v
                    +---------+---------+
                    | Azure Databricks   |
                    | (Aggregation &     |
                    |  Metric Creation)  |
                    +---------+---------+
                              |
                              v
                  +-----------+-----------+
                  | ADLS Gen2 - Gold Layer   |
                  | (Aggregated Metrics CSV) |
                  +-----------+-----------+
                              |
                              v
                        +-----+-----+
                        | Power BI  |
                        | (Reports  |
                        |  & Insights) |
                        +-----------+
```

---

## Key Components

* **Azure Data Factory (ADF):** Ingested customer data from an API endpoint (JSON) and other datasets (stores, products, transactions) from Azure SQL Database. Data was stored in **Azure Data Lake Storage (ADLS Gen2)** in **Parquet format** within the **Bronze layer**.
* **Azure Databricks (PySpark):** Mounted ADLS storage and performed transformations including cleaning, joining, and aggregations. Processed data was moved from **Bronze → Silver → Gold** layers.
* **Power BI:** Downloaded Gold layer CSV data for visualization and built interactive dashboards showing KPIs such as total revenue, top-performing stores, and customer purchase behavior.

---

## Project Requirements

To replicate or run this project on your own machine, ensure the following:

### Prerequisites

* **Azure Subscription** (with permissions for ADF, Databricks, ADLS, and SQL Database)
* **Power BI Desktop** installed locally
* **Databricks Workspace** configured and connected to ADLS Gen2
* **API endpoint** providing customer data in JSON format
* **Azure SQL Database** with tables for `Stores`, `Products`, and `Transactions`

### Technologies Used

* Azure Data Factory
* Azure SQL Database
* Azure Databricks (PySpark)
* Azure Data Lake Storage Gen2
* Power BI
* Python (PySpark)
* SQL

---

## Getting Started

1. **Set up Azure Resources**

   * Create an **Azure SQL Database** and load data for products, stores, and transactions.
   * Set up **ADLS Gen2** and configure container hierarchy: `bronze`, `silver`, `gold`.
   * Deploy **Azure Data Factory** and configure linked services for SQL DB, API, and ADLS.

2. **Data Ingestion with ADF**

   * Create ADF pipelines to pull JSON data from API and SQL data from Azure SQL DB.
   * Store the raw data in the **Bronze layer** (Parquet format).

3. **Data Processing with Databricks**

   * Mount ADLS Gen2 in Databricks using credentials.
   * Use **PySpark** to clean and join datasets (customers, transactions, stores, products).
   * Store the cleaned dataset in the **Silver layer**.
   * Perform aggregations and load results into the **Gold layer**.

4. **Visualization with Power BI**

   * Download the aggregated data (CSV) from the Gold layer.
   * Build Power BI dashboards to visualize key retail metrics and insights.

---

## Deliverables

* **ETL Pipelines:** Automated ingestion and transformation using ADF and Databricks.
* **Data Lake Storage:** Organized Medallion Architecture (Bronze, Silver, Gold).
* **Power BI Dashboard:** Retail performance insights with metrics on sales, customers, and products.
* **Documentation:** Setup instructions and architecture overview.

---

## Outcome

This project highlights a robust, scalable, and cloud-based data engineering workflow using the Azure ecosystem. It efficiently integrates multiple data sources, ensures clean and structured data flow through the Medallion Architecture, and delivers actionable insights through Power BI visualizations.
