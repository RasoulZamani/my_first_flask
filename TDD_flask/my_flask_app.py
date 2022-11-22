import statuses

from flask import Flask

COUNTERS = {}
app = Flask(__name__)

@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """ create counter"""
    app.logger.info(f"Request to create counter {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"message": f"Counter {name} already exists!"}, statuses.HTTP_409_CONFLICT
    COUNTERS[name] = 0 
    return {name:  COUNTERS[name]}, statuses.HTTP_201_CREATED

    