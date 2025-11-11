FROM python:3.13-slim

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files for layer caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY monetary_policy_api.py /app/
COPY monetary_policy_tools.py /app/
COPY server.py /app/

# Create non-root user and set permissions
RUN adduser --system --group --home /home/app app && \
    chown -R app:app /app

ENV HOME=/home/app
USER app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]
