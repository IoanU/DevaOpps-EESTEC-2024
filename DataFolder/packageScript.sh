#!/bin/bash
# Install all packages offline from the packages directory
pip install --no-index --break-system-packages  --find-links ./packages -r ./requirements.txt

