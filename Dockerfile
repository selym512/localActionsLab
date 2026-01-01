FROM python:3.9-slim

WORKDIR /app

# Install the testing library
RUN pip install pytest snowflake-connector-python

# Copy ALL files (source code AND tests)
COPY src/ .

# Default command (still runs the app)
CMD ["python", "main.py"]
