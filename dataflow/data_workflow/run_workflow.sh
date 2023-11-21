#!/bin/bash

# Navigate to the script directory (replace with your actual directory path)
cd ~/data_workflow

# Run the data retrieval Python script
/usr/bin/python3 get_data.py

# Run the data transformation Python script
/usr/bin/python3 transform_data.py
