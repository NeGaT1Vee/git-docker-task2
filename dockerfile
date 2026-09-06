from python:3.12-slim

workdir /app

copy requirements.txt .

run pip install --no-cache-dir -r requirements.txt 

copy src/ ./src/
copy data/ ./data/

cmd ["python", "src/pipeline.py"]