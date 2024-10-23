FROM python:3.13.0-slim

RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0"]
