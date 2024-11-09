#!/bin/bash
# Install all packages offline from the packages folder
pip install --no-index --find-links /usr/src/app/DataFolder/packages -r /usr/src/app/requirements.txt
