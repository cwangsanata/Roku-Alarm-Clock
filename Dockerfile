#syntax=docker/dockerfile:1

FROM python:3.12-bookworm
WORKDIR /src
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "src/app.py"]