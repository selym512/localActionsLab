FROM python:3.9-slim

WORKDIR /app

# Install the testing library
RUN pip install pytest snowflake-connector-python

# Copy ALL files
COPY . .

# Default command
CMD ["python", "main.py"]


