FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN pip install pip --upgrade
RUN pip install -r requirements.txt

RUN chmod +x run.sh

CMD ["./run.sh"]