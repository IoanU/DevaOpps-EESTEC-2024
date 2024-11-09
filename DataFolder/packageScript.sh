#!/bin/bash

# Set the packages and requirements paths based on the current script location
if [ -n "$TASK_ENVIRONMENT" ]; then
    # Task environment paths
    PACKAGES_DIR="/usr/src/app/DataFolder/packages"
    REQUIREMENTS_FILE="/usr/src/app/DataFolder/requirements.txt"
else
    # Local environment paths (relative to this script's location)
    BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    PACKAGES_DIR="$BASE_DIR/packages"
    REQUIREMENTS_FILE="$BASE_DIR/requirements.txt"
fi

# Install all packages offline from the packages directory
pip install --no-index --break-system-packages --find-links "$PACKAGES_DIR" -r "$REQUIREMENTS_FILE"
