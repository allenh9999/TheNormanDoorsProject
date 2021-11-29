import flask
import arrow
import WorkoutBuddies


@WorkoutBuddies.app.route('/api/u/<username>/', methods=['GET'])
def user_name_api(username):
    connection = WorkoutBuddies.model.get_db()
    user = connection.execute("SELECT * from users where username = ?",(username,)).fetchall()
    if len(user) == 0:
        return flask.jsonify(**{"message": "Not Found", "status_code": 404}), 404
    total_minutes = 0
    total_calories = 0
    posts = connection.execute("SELECT * from posts where username = ?",(username,)).fetchall()
    for post in posts:
        seconds = (arrow.get(post['exerciseTime'], 'YYYY-MM-DD HH:mm:ss') - arrow.get(post['created'], 'YYYY-MM-DD HH:mm:ss')).total_seconds()
        minutes = int(seconds // 60)
        total_minutes+=minutes
        total_calories+=WorkoutBuddies.api.feed.get_calories(post['exercise'],minutes)
    context = {
        "total_minutes": total_minutes,
        "total_calories": total_calories,
        "first_name":user[0]['firstname'],
        "last_name":user[0]['lastname'],
        "created": arrow.get(user[0]['creation']).humanize()
    }
    return flask.jsonify(**context)