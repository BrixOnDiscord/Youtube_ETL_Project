# YouTube ETL Project

## Overview
This project implements an ETL pipeline that extracts data on the top 20 viral YouTube videos in the US, cleans and transforms the data, and outputs a CSV file with the processed results.

## Technologies Used
- Python (for scripting ETL logic)
- Apache Airflow (for scheduling and orchestration)
- YouTube Data API (for data extraction)
- Pandas (for data transformation and cleaning)

## Project Motivation
This is a personal project developed to apply and test skills acquired in data engineering, including API integration, data processing, and pipeline orchestration.

## Project Scope and Limitations
Originally, the project was intended to include a loading step that inserts the processed data into a PostgreSQL database. However, this was postponed due to version conflicts with Apache Airflow in the current development environment.

## How to Use
1. Configure Airflow and provide valid YouTube API credentials.
2. Run the DAG to automatically fetch, process, and save the CSV output.
3. Output CSV can be found in the designated data folder.



