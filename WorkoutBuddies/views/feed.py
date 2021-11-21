import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/feed/', methods=['GET'])
def feed_page():
    context = { "name": 'Allen' }
    return flask.render_template("feed.html", **context)