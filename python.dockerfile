FROM python:3.10-slim

WORKDIR /code
COPY . /code
CMD ["python3", "/code/run_code_in_docker.py"]
