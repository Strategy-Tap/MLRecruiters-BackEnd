@echo off
echo "exporting...."
poetry export --format requirements.txt > requirements.txt

echo "exporting with development dependencies...."
poetry export --format requirements.txt > full_requirements.txt --dev

