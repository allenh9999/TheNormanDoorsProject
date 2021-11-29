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

@WorkoutBuddies.app.route('/api/logout/', methods=["GET"])
def log_out_api():
    if "username" not in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    del flask.session["username"]
    context = { "status": "success" }
    return flask.jsonify(**context)

@WorkoutBuddies.app.route('/api/signup/', methods=["POST"])
def signup_api():
    if 'username' in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    data = flask.request.get_json(force=True)
    fields = ['username', 'firstname', 'lastname', 'email', 'password', 'weight', 'passwordCheck']
    for field in fields:
        if field not in data:
            return flask.jsonify(**{"message": "Bad Request", "status_code": 400}), 400
        if data[field] == '':
            return flask.jsonify(**{"status": "failed", "reason": "empty field"})
    context = {
        "status": "failed",
    }
    # check username
    connection = WorkoutBuddies.model.get_db()
    username = connection.execute("SELECT username FROM users WHERE username = ?", (data["username"],)).fetchall()
    if len(username) != 0:
        context["reason"] = "username duplicate"
        return flask.jsonify(**context)
    for symbol in ['@', ' ']:
        if symbol in data['username']:
            context["reason"] = "username invalid character"
            return flask.jsonify(**context)
    if '@' not in data['email']:
        context["reason"] = "invalid email"
        return flask.jsonify(**context)
    email = connection.execute('SELECT email FROM users WHERE email = ?', (data['email'],)).fetchall()
    if len(email) != 0:
        context['reason'] = 'email duplicate'
        return flask.jsonify(**context)
    if data['password'] != data['passwordCheck']:
        context['reason'] = 'passwords are not same'
        return flask.jsonify(**context)
    try:
        weight = int(data['weight'])
        if weight < 1 or weight > 2000:
            raise ValueError("")
    except ValueError:
        context['reason'] = 'invalid weight'
        return flask.jsonify(**context)
    connection.execute("INSERT INTO users(username, firstname, lastname, email, password, weight) VALUES (?, ?, ?, ?, ?, ?)",
        (data['username'], data['firstname'], data['lastname'], data['email'], data['password'], data['weight']))
    context['status'] = 'success'
    flask.session['username'] = data['username'];
    return flask.jsonify(**context)
