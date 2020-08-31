FROM python:3-slim

WORKDIR /usr/src/liteserver
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "server.py" ]