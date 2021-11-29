import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/u/<username>/', methods=['GET'])
def user_info(username):
    if 'username' not in flask.session:
        return flask.redirect('/') # flask.session.clear() to clear cookies
    
    context = { 
        "name": flask.session['username'], 
        "username": username
        }
    return flask.render_template("userinfo.html", **context)