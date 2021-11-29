import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/creategroup/', methods=['GET'])
def feed_page():
    if 'username' not in flask.session:
        flask.session['username'] = 'allen' # flask.session.clear() to clear cookies
    
    context = { "name": flask.session['username'] }
    return flask.render_template("creategroup.html", **context)