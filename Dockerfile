FROM python:3

ENV FLASK_APP=src

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]
