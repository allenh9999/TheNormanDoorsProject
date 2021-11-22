'''A lot of this code template can be found at https://eecs485staff.github.io/eecs485.org/'''
import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'A\x92\x06\xd7Y\xc7\xecI\xe7\xb3t:6\x8f\xe5\x9e\x98#\xa5S\x8a\x99\xc9\xe8' # change if deploying to server
SESSION_COOKIE_NAME = 'login'

DATABASE_FILENAME = pathlib.Path(__file__).resolve().parent.parent / 'var' / 'WorkoutBuddies.sqlite3'
