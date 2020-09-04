FROM python:3

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y libgdal-dev

ENV CPLUS_INCLUDE_PATH=/usr/inulcde/gdal
ENV C_INCLUDE_PATH=/usr/inulcde/gdal

COPY requirements/development.txt ./
RUN pip install --no-cache-dir -r development.txt

COPY . .
RUN chmod +x start.sh
RUN chmod +x auto_hold.sh

