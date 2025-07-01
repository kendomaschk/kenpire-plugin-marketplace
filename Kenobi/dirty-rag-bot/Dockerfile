FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y \
    ffmpeg \
    libsndfile1 \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama pull dolphin-mixtral

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["bash", "-c", "python3 main.py & cd ui && python3 -m http.server 8081"]
