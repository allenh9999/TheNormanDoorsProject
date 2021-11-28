import flask
import WorkoutBuddies


@WorkoutBuddies.app.route('/settings/', methods=['GET'])
def settings_page():
    if 'username' not in flask.session:
        return flask.redirect('/')
    context = {'name': flask.session['username']}
    return flask.render_template("settings.html", **context)