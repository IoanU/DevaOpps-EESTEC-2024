#!/bin/bash
# Setup script for DevaOpps project

echo "🚀 Setting up DevaOpps environment..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

echo "✅ Setup complete!"
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate   # On Linux/Mac"
echo "  venv\\Scripts\\activate    # On Windows"
