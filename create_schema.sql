DROP TABLE Professor;
CREATE TABLE Professor (
  professorId INTEGER NOT NULL,
  firstName VARCHAR(30) NOT NULL,
  lastName VARCHAR(30) NOT NULL,
  PRIMARY KEY (professorId)
);

DROP TABLE Course;
CREATE TABLE Course (
  courseId INTEGER NOT NULL,
  courseName VARCHAR(30) NOT NULL,
  courseNumber VARCHAR(30) NOT NULL,
  PRIMARY KEY (courseId)
);

DROP TABLE CourseReview;
CREATE TABLE CourseReview (
  reviewId INTEGER NOT NULL,
  courseId INTEGER NOT NULL,
  professorId INTEGER NOT NULL,
  review VARCHAR(30) NOT NULL,
  rating INTEGER NOT NULL,
  reviewDate DATE NOT NULL,
  PRIMARY KEY (reviewId),
  FOREIGN KEY (courseId) REFERENCES Course(courseId),
  FOREIGN KEY (professorId) REFERENCES Professor(professorId)
  ON DELETE CASCADE
);
