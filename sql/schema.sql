PRAGMA foreign_keys = ON;

CREATE TABLE users(
   username VARCHAR(20) NOT NULL,
   firstname VARCHAR(40) NOT NULL,
   lastname VARCHAR(40) NOT NULL,
   email VARCHAR(40) NOT NULL,
   password VARCHAR(256) NOT NULL,
   creation DATETIME DEFAULT CURRENT_TIMESTAMP,
   weight INTEGER NOT NULL,
   PRIMARY KEY(username)
);

CREATE TABLE posts(
	id INTEGER NOT NULL,
	username VARCHAR(20) NOT NULL,
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
   exercise VARCHAR(20) NOT NULL,
   exerciseTime DATETIME NOT NULL,
   description VARCHAR(1024) NOT NULL,
	FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE,
	PRIMARY KEY(id)
);

CREATE TABLE groups(
   name VARCHAR(20) NOT NULL,
   password VARCHAR(256) NOT NULL,
   PRIMARY KEY(name)
);

CREATE TABLE in_group(
   username VARCHAR(20) NOT NULL,
   groupname VARCHAR(20) NOT NULL,
   FOREIGN KEY(groupname) REFERENCES groups(name) ON DELETE CASCADE,
   FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE,
   PRIMARY KEY(username, groupname)
);

CREATE TABLE exercise(
   name VARCHAR(40) NOT NULL,
   calRate FLOAT,
   PRIMARY KEY(name)
);