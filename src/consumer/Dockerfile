FROM python:3.10.11-bullseye

WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "consumer.py"]
