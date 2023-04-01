FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update
RUN apt install git -y
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./log.ini /code/app/log.ini

CMD ["uvicorn", "app.main:app", \
     "--host", "0.0.0.0",       \
     "--port", "8000",          \
     "--log-config", "/code/app/log.ini", \
     "--proxy-headers"]
