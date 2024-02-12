FROM python:latest

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

CMD python3 ./app.py