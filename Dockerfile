FROM python:latest
FROM doxygen/doxygen:latest

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN doxygen Doxyfile

EXPOSE 3001

CMD python3 ./app.py