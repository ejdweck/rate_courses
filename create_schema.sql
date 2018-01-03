DROP TABLE Instructor;
CREATE TABLE Professor (
  instructorId INTEGER NOT NULL,
  firstName VARCHAR(30) NOT NULL,
  lastName VARCHAR(30) NOT NULL,
  PRIMARY KEY (instructorId)
);

DROP TABLE Course;
CREATE TABLE Course (
  courseName VARCHAR(30) NOT NULL,
  courseDepartment VARCHAR(30) NOT NULL,
  courseNumber VARCHAR(30) NOT NULL,
  averageRating DOUBLE, 
  PRIMARY KEY (courseDepartment, courseNumber),
  FOREIGN KEY (courseDepartment, courseNumber) REFERENCES GradePoint (courseId)
  ON DELETE CASCADE
);

DROP TABLE GradePoint;
CREATE TABLE GradePoint (
  courseId VARCHAR(30) NOT NULL,
  fallSem15 DOUBLE,
  springSem15 DOUBLE,
  fallSem16 DOUBLE,
  springSem16 DOUBLE,
  fallSem16 DOUBLE,
  springSem16 DOUBLE,
  PRIMARY KEY (courseId)
);

DROP TABLE CourseReview;
CREATE TABLE CourseReview (
  reviewId INTEGER NOT NULL,
  courseId VARCHAR(30) NOT NULL,
  professorId INTEGER NOT NULL,
  reviewerId INTEGER NOT NULL,
  review VARCHAR(100) NOT NULL,
  rating INTEGER NOT NULL,
  reviewDate DATE NOT NULL,
  PRIMARY KEY (reviewId),
  FOREIGN KEY (courseId) REFERENCES Course(courseDepartment, courseNumber),
  FOREIGN KEY (professorId) REFERENCES Professor(professorId)
  ON DELETE CASCADE
);
