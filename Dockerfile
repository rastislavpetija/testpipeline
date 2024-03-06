FROM python:3.9-slim

COPY . /opt/apps/web_server
WORKDIR /opt/apps/web_server
# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Run the Flask app
CMD ["python", "main.py"]
