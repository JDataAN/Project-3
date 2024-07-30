# Data Extraction & Storage

This branch focuses on extracting and storing influenza data from the CDC's website to support our flu data analysis and visualization. The data found in this branch is directly sourced from the CDC's website: [CDC Flu Data](https://www.cdc.gov/flu/weekly/usmap.htm).

## Contents

### 1. Data Extraction and Storage
This document details the overall scope of this branch, including the methods and processes used for data extraction and storage. It outlines the steps taken to retrieve data from the CDC's website and store it in a structured format.

### 2. API and Flask Application
**File:** `app.py`

This script contains the Flask application used to create an API for accessing the flu data. The API provides endpoints to fetch overall flu data for the U.S., making it easy to integrate with other services and applications.

### 3. Daily Data Update
**File:** `update_data.py`

This script includes the code for a scheduling tool that updates the flu data on a daily basis. It ensures that our API and map visualization are always using the most recent data available.

### 4. State Data Database
**Folder:** `instance`

This folder contains the SQLite3 database (`state_data.db`) that was created to store the state-level flu data. The database is designed to be lightweight and efficient for quick data retrieval.

## Summary

This branch represents the foundational work for data extraction and storage, ensuring that our flu data analysis is based on the most up-to-date information. Joy Ragland led the efforts in this branch, implementing the data extraction scripts, setting up the Flask API, and creating the scheduling tool for daily updates.

