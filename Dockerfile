FROM python:3.8-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install \
    'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

COPY .. . 
RUN pip install -r requirements_client.txt

EXPOSE 8501

CMD ["streamlit", "run", "src/client.py"]