#!/bin/bash

# Replace with your actual Markdown file path
FILE_PATH="/home/tom/datalinux-labs-2324-TomDeloddere/dataflow/data_workflow/report.md"
PDF_OUTPUT="/home/tom/datalinux-labs-2324-TomDeloddere/dataflow/data_workflow/report.PDF"

# Watching for changes in the Markdown file
while inotifywait -e close_write $FILE_PATH; do
    pandoc "$FILE_PATH" -o "$PDF_OUTPUT"
    echo "PDF generated at $(date)"
done

