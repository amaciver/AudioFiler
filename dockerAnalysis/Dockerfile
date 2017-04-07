FROM scivm/scientific-python-2.7

# Grab requirements.txt
ADD ./analysis_backend/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD ./analysis_backend /opt/analysis_backend
WORKDIR /opt/analysis_backend

CMD gunicorn --bind 0.0.0.0:$PORT wsgi

