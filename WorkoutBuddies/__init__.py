import flask

app = flask.Flask(__name__)


app.config.from_object('WorkoutBuddies.config')

import WorkoutBuddies.views