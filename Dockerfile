FROM python:3.7-alpine

ENV FLASK_APP bot.py
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 3000

COPY app /app
COPY requirements.txt /requirements.txt

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip3 install -r /requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["/app/bot.py"]