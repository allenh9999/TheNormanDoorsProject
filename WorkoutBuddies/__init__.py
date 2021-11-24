'''A lot of this code template can be found at https://eecs485staff.github.io/eecs485.org/'''
import flask

app = flask.Flask(__name__)


app.config.from_object('WorkoutBuddies.config')

import WorkoutBuddies.views
import WorkoutBuddies.api
import WorkoutBuddies.model
