FROM python:3.11-slim
WORKDIR /app
COPY aprs.py .
CMD ["python", "aprs.py"]
