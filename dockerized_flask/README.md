# dockerized simple flask app

create directory named web. then copy app.py there:

```
# app.py
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hi():
    return "hello from dockerized  flask to dirty world!"


    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True, port=5000)

```

and then create requirement.txt including libs (in here just Flask!)

for Dockerfile start from python (3.6 for better compability recomended),  write:

```
from python:3.6
WORKDIR /usr/src/app
COPY requirement.txt .
RUN pip install --no-cache-dir  -r requirement.txt
COPY app.py .
CMD ["python","app.py"]
```

you can now build image by 
```
docker build -t img_name:tag 
````

but if you want run a service by docker compose ( it make sence when you have more than one service) back to parent directory and create docker-compose file:
```
version: '3'
services:
  web:
    build: ./web
    ports:
      - "5000:5000"
```

and then type:
```
docker compose build
docker compose up
```
congragulations! your app is up!!
