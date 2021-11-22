PRAGMA foreign_keys = ON;

INSERT INTO users(username, firstname, lastname, email, password)
VALUES ('allen', 'Allen', 'Ho', 'hoal@umich.edu', 'password');

INSERT INTO users(username, firstname, lastname, email, password)
VALUES ('tajes', 'Tajes', 'Khanna', 'tkhanna@umich.edu', 'password');

INSERT INTO posts(id, username, exercise, exerciseTime, description)
VALUES (0, 'allen', 'swimming', CURRENT_TIMESTAMP, 'I was swimming for 30 minutes');

INSERT INTO posts(id, username, exercise, exerciseTime, description)
VALUES (1, 'tajes', 'running', CURRENT_TIMESTAMP, 'Ran for 40 minutes');

INSERT INTO groups(name, password)
VALUES ('493 gains', 'password');

INSERT INTO in_group(username, groupname)
VALUES ('allen', '493 gains');

INSERT INTO in_group(username, groupname)
VALUES ('tajes', '493 gains');
