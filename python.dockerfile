FROM python:3.10-slim

WORKDIR /code
COPY . /code
CMD ["python3", "/code/app2.py"]
