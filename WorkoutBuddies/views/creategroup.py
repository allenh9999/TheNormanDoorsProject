import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/creategroup/', methods=['GET'])
def create_group():
    if 'username' not in flask.session:
        return flask.redirect('/') # flask.session.clear() to clear cookies
    
    context = { "name": flask.session['username'] }
    return flask.render_template("creategroup.html", **context)