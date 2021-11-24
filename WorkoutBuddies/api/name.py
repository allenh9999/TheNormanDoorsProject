import flask
import WorkoutBuddies

def get_name(username):
    return WorkoutBuddies.model.get_db().execute("SELECT firstname, lastname FROM users where username = ?", (username,)).fetchall()

@WorkoutBuddies.app.route('/api/name/', methods=['GET'])
def get_name_api():
    if "username" not in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    context = {}
    name = get_name(flask.session["username"])
    if len(name) == 0:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    return flask.jsonify(**name[0])