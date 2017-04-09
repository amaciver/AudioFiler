FROM scivm/scientific-python-2.7

RUN apt-get -y update && apt-get install -y libatlas-base-dev gfortran python-numpy python-scipy
RUN apt-get install -y python-pip
RUN pip install numpy --upgrade

# Grab requirements.txt
ADD ./analysis_backend/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -r /tmp/requirements.txt
RUN pip install gunicorn

# Add our code
ADD ./analysis_backend /opt/analysis_backend
WORKDIR /opt/analysis_backend

EXPOSE 8000

# Install additional dependencies
RUN apt-get -y install ffmpeg libav-tools
RUN pip install eyed3 pydub six pyparsing cycler packaging hmmlearn functools32

RUN useradd -m myuser
USER myuser

CMD gunicorn analysis_backend.wsgi:application --bind 0.0.0.0:$PORT
