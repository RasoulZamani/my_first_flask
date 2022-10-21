from python:3.6
WORKDIR /usr/src/app
COPY requirement.txt .
RUN pip install --no-cache-dir  -r requirement.txt
COPY app.py .
CMD ["python","app.py"]

