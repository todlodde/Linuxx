#!/bin/bash

# URL of the dataset
DATA_URL="https://fred.stlouisfed.org/data/DGS10.txt"

# Create a directory for data
mkdir -p data

# Filename with current date and time
FILENAME="data/$(date +%Y%m%d-%H%M%S)-DGS10.txt"

# Download the data
curl -o "$FILENAME" "$DATA_URL"
