# Mobileye Data Engineer Home Test

## Overview

This Python process is designed to monitor for the arrival of new JSON files containing data from Mobileye's objects detection and vehicle status systems. Upon detecting new files, the process parses the JSON data, inserts it into corresponding tables in a PostgreSQL database, and removes the processed files.

## Prerequisites

- Python 3.x installed on your system.
- PostgreSQL database server installed and running.
- Required Python packages installed (can be installed via `pip`):
  - `pandas`
  - `psycopg2-binary`
  - `sqlalchemy`

## Configuration

1. **Database Configuration**:
   - Edit the `engine` variable in the Python script (`main.py`) to match your PostgreSQL database connection parameters.

2. **JSON Files**:
   - Place the JSON files (`objects_detection.json` and `vehicles_status.json`) from `files_backup` directory containing the data to be processed in the `input` directory as the Python script.

## Running the Process

1. Ensure that the PostgreSQL database server is running.

2. Open a terminal or command prompt and navigate to the directory containing the Python script (`main.py`) and the JSON files.

3. Run the Python script using the following command:

   ```
   python main.py
   ```

4. The process will continuously monitor for new JSON files and load them into the corresponding tables in the database.

5. Press `Ctrl + C` to stop the process.

## Notes

- Ensure that the JSON files adhere to the provided format for objects detection and vehicle status data.
- The script will automatically remove processed JSON files from the directory.


For any questions or issues, please [contact me](mailto:idan.bushari@gmail.com).

---
