'''A lot of this code template can be found at https://eecs485staff.github.io/eecs485.org/'''
import sqlite3
import flask
import WorkoutBuddies


def get_db():
    if 'sqlite_db' not in flask.g:
        flask.g.sqlite_db = sqlite3.connect(
            str(WorkoutBuddies.app.config['DATABASE_FILENAME']))
        flask.g.sqlite_db.row_factory = lambda cursor, row: {
            col[0]: row[idx] for idx, col in enumerate(cursor.description)}
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db


@WorkoutBuddies.app.teardown_appcontext
def close_db(error):
    assert error or not error
    sqlite_db = flask.g.pop('sqlite_db', None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()
