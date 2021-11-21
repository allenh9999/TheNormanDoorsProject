import flask
import NormanDoors


@NormanDoors.app.route('/', methods=['GET'])
def main_page():
    context = {}
    return flask.render_template("main.html", **context)