FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

COPY ./requirements.txt /app/requirements.txt
COPY ./requirements-dev.txt /app/requirements-dev.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements-dev.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["/start-reload.sh"]