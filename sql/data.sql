PRAGMA foreign_keys = ON;

INSERT INTO users(username, firstname, lastname, email, password, weight)
VALUES ('allen', 'Allen', 'Ho', 'hoal@umich.edu', 'password', 140);

INSERT INTO users(username, firstname, lastname, email, password, weight)
VALUES ('tajes', 'Tajes', 'Khanna', 'tkhanna@umich.edu', 'password', 140);

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

--From https://whatscookingamerica.net/information/calorieburnchart.htm

INSERT INTO exercise(name, calRate)
VALUES('playing badminton', 0.044);

INSERT INTO exercise(name, calRate)
VALUES('playing basketball', 0.063);

INSERT INTO exercise(name, calRate)
VALUES('bicycling', 0.037);

INSERT INTO exercise(name, calRate)
VALUES('bicycling (around 5 mph)', 0.029);

INSERT INTO exercise(name, calRate)
VALUES('bicycling (around 10 mph)', 0.045);

INSERT INTO exercise(name, calRate)
VALUES('climbing', 0.058);

INSERT INTO exercise(name, calRate)
VALUES('climbing (no load)', 0.055);

INSERT INTO exercise(name, calRate)
VALUES('climbing (10 lb load)', 0.058);

INSERT INTO exercise(name, calRate)
VALUES('climbing (20 lb load)', 0.064);

INSERT INTO exercise(name, calRate)
VALUES('cooking', 0.022);

INSERT INTO exercise(name, calRate)
VALUES('dancing', 0.046);

INSERT INTO exercise(name, calRate)
VALUES('dancing (ballroom)', 0.023);

INSERT INTO exercise(name, calRate)
VALUES('dancing (aerobic medium)', 0.046);

INSERT INTO exercise(name, calRate)
VALUES('dancing (aerobic intense)', 0.061);

INSERT INTO exercise(name, calRate)
VALUES('doing an abs workout', 0.033);

INSERT INTO exercise(name, calRate)
VALUES('doing an abdominal workout', 0.033);

INSERT INTO exercise(name, calRate)
VALUES('golfing', 0.038);

INSERT INTO exercise(name, calRate)
VALUES('grocery shopping', 0.028);

INSERT INTO exercise(name, calRate)
VALUES('jogging', 0.087);

INSERT INTO exercise(name, calRate)
VALUES('jumping rope', 0.080);

INSERT INTO exercise(name, calRate)
VALUES('mowing the lawn', 0.051);

INSERT INTO exercise(name, calRate)
VALUES('playing raquetball', 0.081);

INSERT INTO exercise(name, calRate)
VALUES('raking leaves', 0.025);

INSERT INTO exercise(name, calRate)
VALUES('running', 0.095);

INSERT INTO exercise(name, calRate)
VALUES('running (6 minute mile)', 0.115);

INSERT INTO exercise(name, calRate)
VALUES('running (8 minute mile)', 0.095);

INSERT INTO exercise(name, calRate)
VALUES('running (9 minute mile)', 0.087);

INSERT INTO exercise(name, calRate)
VALUES('sitting', 0.009);

INSERT INTO exercise(name, calRate)
VALUES('skiing', 0.065);

INSERT INTO exercise(name, calRate)
VALUES('skiing (downhill)', 0.065);

INSERT INTO exercise(name, calRate)
VALUES('skiing (uphill)', 0.125);

INSERT INTO exercise(name, calRate)
VALUES('snowshoeing', 0.075);

INSERT INTO exercise(name, calRate)
VALUES('squatting', 0.095);

INSERT INTO exercise(name, calRate)
VALUES('swimming', 0.064);

INSERT INTO exercise(name, calRate)
VALUES('swimming (slow)', 0.058);

INSERT INTO exercise(name, calRate)
VALUES('swimming (fast)', 0.071);

INSERT INTO exercise(name, calRate)
VALUES('swimming (breast stroke, fast)', 0.074);

INSERT INTO exercise(name, calRate)
VALUES('playing table tennis', 0.031);

INSERT INTO exercise(name, calRate)
VALUES('playing ping pong', 0.031);

INSERT INTO exercise(name, calRate)
VALUES('walking', 0.036);

INSERT INTO exercise(name, calRate)
VALUES('walking (flat road)', 0.036);

INSERT INTO exercise(name, calRate)
VALUES('walking (hills/fields)', 0.037);

INSERT INTO exercise(name, calRate)
VALUES('weeding', 0.033);

INSERT INTO exercise(name, calRate)
VALUES('weight training', 0.039);

INSERT INTO exercise(name, calRate)
VALUES('weight training (free weights)', 0.039);

INSERT INTO exercise(name, calRate)
VALUES('weight training (circuit training)', 0.042);
