FROM continuumio/anaconda3

ADD ./model_backend/requirements.txt /tmp/requirements.txt
ADD ./model_backend/package.json /tmp/package.json

RUN apt-get install -y npm
RUN cd /tmp && npm install
RUN cd ..
RUN pip install -qr /tmp/requirements.txt

ADD ./model_backend /opt/model_backend
WORKDIR /opt/model_backend

CMD gunicorn model_backend.wsgi:application --bind 0.0.0.0:$PORT
