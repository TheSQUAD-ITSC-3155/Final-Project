DROP DATABASE IF EXISTS Reddit;

CREATE DATABASE IF NOT EXISTS Reddit;

USE Reddit;

CREATE TABLE IF NOT EXISTS Person (
	/*User_Id INT AUTO_INCREMENT NOT NULL,*/
    User_Id INT NOT NULL,
	Username VARCHAR(255) NOT NULL,
    Picture_Id INT NOT NULL,
    PRIMARY KEY (User_Id)
);
INSERT INTO Person (User_Id, Username, Picture_Id)
VALUES
    (0, 'GrantMorrigan33', 1),
    (1, 'WallFace', 5)
;
select * from Person;

CREATE TABLE IF NOT EXISTS Post (
	/*Post_Id INT AUTO_INCREMENT NOT NULL,*/
    Post_Id INT NOT NULL,
    C_Name VARCHAR(255) NOT NULL,
	User_Id INT NULL,
    Words VARCHAR(255) NOT NULL,
    PRIMARY KEY (Post_Id),
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE SET NULL
);
INSERT INTO Post (Post_Id, C_Name, User_Id, Words)
VALUES
    (0, 'Why', 0, 'I hurt in the shower.'),
    (1, 'Do', 1, 'You feel it?')
;
select * from Post;

CREATE TABLE IF NOT EXISTS C_Comment (
	Comment_Id INT NOT NULL,
    Post_Id INT NULL,
    User_Id INT NULL,
    Words VARCHAR(255) NOT NULL,
    PRIMARY KEY (Comment_Id),
    FOREIGN KEY (Post_Id) REFERENCES Post(Post_Id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE SET NULL
);

INSERT INTO C_Comment (Comment_Id, Post_Id, User_Id, Words)
VALUES
    (0, 0, 0,'Lol'),
    (1,1,1,'Thats Dumb')
;
select * from C_Comment;

CREATE TABLE IF NOT EXISTS liked_comments (
    User_Id INT NOT NULL,
    Comment_Id INT NOT NULL,
    PRIMARY KEY (User_Id, Comment_Id),
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Comment_Id) REFERENCES C_Comment(Comment_Id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO liked_comments (User_Id, Comment_Id)
VALUES
    (1, 1),
    (0,0)
; 
select * from liked_comments;

CREATE TABLE IF NOT EXISTS liked_posts (
    User_Id INT NOT NULL,
    Post_Id INT NOT NULL,
    PRIMARY KEY (User_Id, Post_Id),
    FOREIGN KEY (User_Id) REFERENCES Person(User_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Post_Id) REFERENCES Post(Post_Id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO liked_posts (User_Id, Post_Id)
VALUES
    (0, 1),
    (1,0)
; 

select * from liked_posts;