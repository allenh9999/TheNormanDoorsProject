PRAGMA foreign_keys = ON;

INSERT INTO users(username, firstname, lastname, email, password)
VALUES ('allen', 'Allen', 'Ho', 'hoal@umich.edu', 'password');

INSERT INTO users(username, firstname, lastname, email, password)
VALUES ('tajes', 'Tajes', 'Khanna', 'tkhanna@umich.edu', 'password');

INSERT INTO posts(id, username, exercise, exerciseTime, description)
VALUES (0, 'allen', 'swimming', datetime('now', '+30 minute'), 'I was swimming for 30 minutes');

INSERT INTO posts(id, username, exercise, exerciseTime, description)
VALUES (1, 'tajes', 'running', datetime('now', '+40 minute'), 'Ran for 40 minutes');

INSERT INTO groups(name, password)
VALUES ('493 gains', 'password');

INSERT INTO groups(name, password)
VALUES ('493 exercise', 'password');

INSERT INTO in_group(username, groupname)
VALUES ('allen', '493 gains');

INSERT INTO in_group(username, groupname)
VALUES ('tajes', '493 exercise');

INSERT INTO in_group(username, groupname)
VALUES ('allen', '493 exercise');