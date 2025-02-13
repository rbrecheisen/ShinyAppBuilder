#!/bin/bash

# Get the absolute path to the script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
R_HOME="$SCRIPT_DIR/R-Portable"

# Check if the portable R installation exists
if [ -x "$R_HOME/bin/Rscript" ]; then
    # Use the portable R version to run the app
    "$R_HOME/bin/Rscript" run_app.R
else
    echo "Portable R not found in $R_HOME"
    echo "Please ensure that the R-Portable directory exists and contains a working R installation."
    exit 1
fi
