# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Set environment variables to optimize Python performance
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies first to leverage Docker's cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
RUN mkdir -p data

# Expose the port FastAPI will run on
EXPOSE 8000

# Start the application using Uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]