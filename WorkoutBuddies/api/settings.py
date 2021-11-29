import flask
import WorkoutBuddies

@WorkoutBuddies.app.route('/api/settings/', methods=['POST'])
def get_settings_api():
    if "username" not in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    context = {
        "status": "failed",
    }
    connection = WorkoutBuddies.model.get_db()
    data = flask.request.get_json(force=True)
    fields = ['firstname', 'lastname', 'email', 'password', 'weight']
    if "field" not in data or "value" not in data:
        return flask.jsonify(**{"message": "Bad request", "status_code": 400}), 400
    field = data["field"].lower().replace(" ", "")
    if field not in fields:
        return flask.jsonify(**{"message": "Bad request", "status_code": 400}), 400
    if data['value'] == '':
        context['reason'] = "Blank field"
        return flask.jsonify(**context)
    if field == 'password':
        if "passwordCheck" not in data:
            context["reason"] = "no password check"
            return flask.jsonify(**context)
        if data['value'] != data['passwordCheck']:
            context["reason"] = "passwords do not match"
            return flask.jsonify(**context)
        if "passwordOld" not in data:
            context["reason"] = "No old password"
            return flask.jsonify(**context)
        password = connection.execute("SELECT password FROM users WHERE username = ?", (flask.session["username"],)).fetchall()[0]["password"]
        if password != data['passwordOld']:
            context["reason"] = "Old password wrong"
            return flask.jsonify(**context)
    connection.execute("UPDATE users SET {} = ? WHERE username = ?".format(field), (data['value'], flask.session['username']))
    context['status'] = 'success'
    context['value'] = data['value']
    return flask.jsonify(**context)

@WorkoutBuddies.app.route('/api/settings/', methods=['GET'])
def get_user_data():
    if "username" not in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    connection = WorkoutBuddies.model.get_db()
    return flask.jsonify(**connection.execute("SELECT * FROM users WHERE username = ?", (flask.session["username"],)).fetchall()[0])