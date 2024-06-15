# Use the official Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/
# Install any required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /app/
COPY memos_webhook /app/memos_webhook

# Make port 8000 available to the environment outside this container
EXPOSE 8000

# Run main.py when the container launches
CMD ["python", "main.py"]
