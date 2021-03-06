import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/feed/', methods=['GET'])
def feed_page():
    if 'username' not in flask.session:
        flask.redirect('/') # flask.session.clear() to clear cookies
    
    context = { "name": flask.session['username'] }
    return flask.render_template("feed.html", **context)