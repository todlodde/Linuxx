#!/bin/bash

# Navigate to the script directory (replace with your actual directory path)
cd ~/datalinux-labs-2324-TomDeloddere/dataflow/data_workflow

# Run the data retrieval Python script
/usr/bin/python3 get_data.py

# Run the data transformation Python script
/usr/bin/python3 transform_data.py

# Run the data analysis Python script (which now also updates the report)
/usr/bin/python3 analyze_data.py
