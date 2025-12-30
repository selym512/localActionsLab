FROM python:3.9-slim

WORKDIR /app

# Install the testing library
RUN pip install pytest

# Copy ALL files (source code AND tests)
COPY src/ .

# Default command (still runs the app)
CMD ["python", "main.py"]
