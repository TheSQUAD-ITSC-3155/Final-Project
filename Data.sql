DROP DATABASE IF EXISTS Reddit;

CREATE DATABASE IF NOT EXISTS Reddit;

USE Reddit;

SET FOREIGN_KEY_CHECKS=0;

CREATE TABLE IF NOT EXISTS Person (
	User_Id INT AUTO_INCREMENT NOT NULL,
	Username VARCHAR(255) NOT NULL,
    Picture_Id INT NOT NULL,
    PRIMARY KEY (User_Id)
);

CREATE TABLE IF NOT EXISTS Post (
	Post_Id INT AUTO_INCREMENT NOT NULL,
    C_Name VARCHAR(255) NOT NULL,
	User_Id INT NULL,
    Words VARCHAR(255) NOT NULL,
    PRIMARY KEY (Post_Id),
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS C_Comment (
	Comment_Id INT AUTO_INCREMENT NOT NULL,
    Post_Id INT NULL,
    Words VARCHAR(255) NOT NULL,
    User_Id INT NULL,
    PRIMARY KEY (Comment_Id),
    FOREIGN KEY (Post_Id) REFERENCES Post(Post_Id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS liked_comments (
    User_Id INT NOT NULL,
    Comment_Id INT NOT NULL,
    PRIMARY KEY (User_Id, Comment_Id),
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Comment_Id) REFERENCES C_Comment(Comment_Id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS liked_posts (
    User_Id INT NOT NULL,
    Post_Id INT NOT NULL,
    PRIMARY KEY (User_Id, Post_Id),
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Post_Id) REFERENCES Post(Post_Id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Person (Username, Picture_Id)
VALUES
    ('GrantMorrigan33', 1),
    ('WallFace', 5)
;

INSERT INTO Post (C_Name, Words, User_Id)
VALUES
    ('Why', 'I hurt in the shower.', 0),
    ('Need', 'Help with SQL.', 0),
    ('Do', 'You feel it?', 1)
;

INSERT INTO C_Comment (Post_Id, Words, User_Id)
VALUES
    (0,'Lol',1),
    (1,'Thats Dumb.',0)
;

INSERT INTO liked_comments (User_Id, Comment_Id)
VALUES
    (0, 0),
    (1, 0)
; 

INSERT INTO liked_posts (User_Id, Post_Id)
VALUES
    (0, 1),
    (1, 0)
; 