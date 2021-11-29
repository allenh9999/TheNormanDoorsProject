import flask
import WorkoutBuddies

@WorkoutBuddies.app.route('/api/create/', methods=["POST"])
def create_group_api():
    connection = WorkoutBuddies.model.get_db()
    data = flask.request.get_json(force=True)
    if 'name' in data:
        return flask.jsonify(**{"message": "Bad Request", "status_code": 400}), 400
    name = connection.execute("SELECT password, name FROM users WHERE name = ?", (data['name'],)).fetchall()
    if len(name) == 0:
        context = {
            "status": "failed",
            "data": "name"
        }
        return flask.jsonify(**context)
    if len(password) < 1:
        context = {
            "status": "failed",
            "data": "password"
        }
        return flask.jsonify(**context)
    #flask.session['name'] = name[0]['name'];
    context = {
        "status": "success",
    }
    return flask.jsonify(**context)

@WorkoutBuddies.app.route('/api/addgroup/', methods=["POST"])
def add_group_api():
    connection = WorkoutBuddies.model.get_db()
    data = flask.request.get_json(force=True)
    if 'name' not in data:
        return flask.jsonify(**{"message": "Bad Request", "status_code": 400}), 400
    name = connection.execute("SELECT password, name FROM users WHERE name = ?", (data['name'],)).fetchall()
    if len(name) == 0:
        context = {
            "status": "failed",
            "data": "name"
        }
        return flask.jsonify(**context)
    if data['password'] != name[0]['password']:
        context = {
            "status": "failed",
            "data": "password"
        }
        return flask.jsonify(**context)
    #flask.session['name'] = name[0]['name'];
    context = {
        "status": "success",
    }
    return flask.jsonify(**context)