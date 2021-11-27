import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/', methods=['GET'])
def main_page():
    if 'username' in flask.session:
        return flask.redirect('/feed')
    context = {}
    return flask.render_template("main.html", **context)