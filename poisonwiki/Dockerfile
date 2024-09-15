# base image  
FROM python:3.12-slim-bullseye

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED=1  
ENV PYTHONDONTWRITEBYTECODE=1

# Update docker-image packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

# Update pip 
RUN pip install --upgrade pip

# Copy requirements and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir psycopg2-binary && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt \  
    && useradd -U poisonwiki_user \  
    && install -d -m 0777 -o poisonwiki_user -g poisonwiki_user /poisonwiki/staticfiles \
    && install -d -m 0777 -o poisonwiki_user -g poisonwiki_user /poisonwiki/media_root

# Set working directory and user
WORKDIR /poisonwiki
USER poisonwiki_user:poisonwiki_user

# Copy project files
COPY --chown=poisonwiki_user:poisonwiki_user . .


# Expose the application port
EXPOSE 8000

# Set entrypoint
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
