
FROM python:3.10.4

WORKDIR /code

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt 

COPY src/ .s

CMD ["python", "./bot.py"]