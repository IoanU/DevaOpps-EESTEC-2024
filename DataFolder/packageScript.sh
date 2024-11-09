#!/bin/bash

# Define the path to the packages directory and requirements file
PACKAGES_DIR="$(cd "$(dirname "$0")" && pwd)/packages"
REQUIREMENTS_FILE="$(cd "$(dirname "$0")" && pwd)/requirements.txt"

echo "Installing packages from $PACKAGES_DIR..."

# Install packages from the local wheel files
pip install --no-index --break-system-packages --find-links="$PACKAGES_DIR" -r "$REQUIREMENTS_FILE" --user

echo "Package installation completed."
