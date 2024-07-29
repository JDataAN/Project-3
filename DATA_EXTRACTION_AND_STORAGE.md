# Data Extraction and Storage Process

## State Data
The `StateDatabySeasons63_49,48,62.csv` file is cleaned and saved to `Cleaned_StateDatabySeasons63_49,48,62.csv`. The cleaned data is also stored in the SQLite database.

## Periodic Data Updates
The `update_data.py` script is scheduled to run daily to update the data. It uses the `schedule` library to automate the updates.

## Database Schema
The SQLite database `state_data.db` contains the following table:
- `state_data`: Stores the cleaned state data.