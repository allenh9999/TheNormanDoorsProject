import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/', methods=['GET'])
def main_page():
    context = {}
    return flask.render_template("main.html", **context)