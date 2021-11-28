import flask
import WorkoutBuddies

@WorkoutBuddies.app.route('/api/login/', methods=["POST"])
def log_in_api():
    connection = WorkoutBuddies.model.get_db()
    data = flask.request.get_json(force=True)
    if 'username' not in data or 'password' not in data:
        return flask.jsonify(**{"message": "Bad Request", "status_code": 400}), 400
    username = connection.execute("SELECT password, username FROM users WHERE username = ?", (data['username'],)).fetchall()
    if len(username) == 0:
        username = connection.execute("SELECT password, username FROM users WHERE email = ?", (data['username'],)).fetchall()
    if len(username) == 0:
        context = {
            "status": "failed",
            "data": "username"
        }
        return flask.jsonify(**context)
    if data['password'] != username[0]['password']:
        context = {
            "status": "failed",
            "data": "password"
        }
        return flask.jsonify(**context)
    flask.session['username'] = username[0]['username'];
    context = {
        "status": "success",
    }
    return flask.jsonify(**context)