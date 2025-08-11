FROM python:3.11-bookworm

WORKDIR /app
COPY . .

RUN apt-get update && apt-get -y install curl
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [""]
