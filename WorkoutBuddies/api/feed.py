import flask
import WorkoutBuddies
import arrow

def get_groups(username):
    return [group["groupname"] for group in WorkoutBuddies.model.get_db().execute("SELECT groupname FROM in_group WHERE username = ?", (username,)).fetchall()]

@WorkoutBuddies.app.route('/api/feed/', methods=['GET'])
def get_feed_api():
    if "username" not in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    context = {}
    connection = WorkoutBuddies.model.get_db()
    userGroups = set(get_groups(flask.session["username"]))
    usernameGroups = {}
    posts = connection.execute("SELECT * FROM posts").fetchall()
    returnPosts = []
    for post in posts:
        seconds = (arrow.get(post['exerciseTime'], 'YYYY-MM-DD HH:mm:ss') - arrow.get(post['created'], 'YYYY-MM-DD HH:mm:ss')).total_seconds()
        minutes = int(seconds // 60)
        if minutes != 1:
            post["time"] = "{} minutes".format(minutes)
        else:
            post["time"] = "1 minute"
        if post["username"] not in usernameGroups:
            usernameGroups[post["username"]] = get_groups(post["username"])
        post["groups"] = usernameGroups[post["username"]]
        post["calories"] = minutes * 10
        post["name"] = WorkoutBuddies.api.name.get_name(post["username"])[0]["firstname"]
        post["date"] = arrow.get(post['created']).humanize()
        returnPosts.append(post)
        for group in usernameGroups[post["username"]]:
            if group in userGroups:
                break
        else:
            returnPosts.pop()
    returnPosts.reverse()
    context["posts"] = returnPosts
    context["groups"] = list(userGroups)
    return flask.jsonify(**context)

@WorkoutBuddies.app.route('/api/post/', methods=['POST'])
def post():
    if "username" not in flask.session:
        return flask.jsonify(**{"message": "Forbidden", "status_code": 403}), 403
    data = flask.request.get_json(force=True)
    if "exercise" not in data or "time" not in data or "description" not in data:
        return flask.jsonify(**{"message": "Bad Request", "status_code": 400}), 400
    if data["description"] == "":
        data["description"] = "No description."
    try:
        if int(data["time"]) < 0:
            raise ValueError
    except BaseException:
        return flask.jsonify(**{"message": "Bad Request", "status_code": 400}), 400
    connection = WorkoutBuddies.model.get_db()
    postCount = connection.execute("SELECT COUNT(*) FROM posts").fetchall()[0]["COUNT(*)"]
    connection.execute("INSERT INTO posts(id, username, exercise, exerciseTime, description) VALUES (?, ?, ?, ?, ?)", 
        (postCount, flask.session["username"], data["exercise"], arrow.utcnow().shift(minutes=int(data["time"])).format('YYYY-MM-DD HH:mm:ss'), data["description"]))
    return flask.jsonify(**{
        "id": postCount,
        "username": flask.session["username"],
        "exercise": data["exercise"],
        "time": data["time"],
        "description": data["description"],
    })