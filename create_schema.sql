DROP TABLE Instructor;
CREATE TABLE Course_Instructor (
  instructorId INTEGER NOT NULL,
  firstName VARCHAR(30) NOT NULL,
  lastName VARCHAR(30) NOT NULL,
  PRIMARY KEY (instructorId)
);

DROP TABLE Course;
CREATE TABLE Course_Course (
  courseDepartment VARCHAR(30) NOT NULL,
  courseNumber VARCHAR(30) NOT NULL,
  courseName VARCHAR(30) NOT NULL,
  averageRating DOUBLE, 
  numberOfRatings INTEGER,
  FOREIGN KEY (courseDepartment, courseNumber) REFERENCES GradePoint (courseDepartment, courseNumber)
  ON DELETE CASCADE,
  PRIMARY KEY (courseDepartment, courseNumber)
);

DROP TABLE GradePoint;
CREATE TABLE Course_GradePoint (
  courseDepartment VARCHAR(30) NOT NULL,
  courseNumber VARCHAR(30) NOT NULL,
  fallSem15 DOUBLE,
  springSem15 DOUBLE,
  fallSem16 DOUBLE,
  springSem16 DOUBLE,
  fallSem17 DOUBLE,
  springSem17 DOUBLE,
  FOREIGN KEY (courseDepartment, courseNumber) REFERENCES Course (courseDepartment, courseNumber),
  PRIMARY KEY (courseDepartment, courseNumber)
);

DROP TABLE CourseReview;
CREATE TABLE Course_CourseReview (
  courseDepartment VARCHAR(30) NOT NULL,
  courseNumber VARCHAR(30) NOT NULL,
  reviewId INTEGER NOT NULL,
  instructorId INTEGER NOT NULL,
  reviewerId INTEGER NOT NULL,
  review VARCHAR(100) NOT NULL,
  rating INTEGER NOT NULL,
  reviewDate DATE NOT NULL,
  FOREIGN KEY (courseDepartment, courseNumber) REFERENCES Course (courseDepartment, courseNumber)
  ON DELETE CASCADE,
  FOREIGN KEY (instructorId) REFERENCES Instructor(instructorId)
  ON DELETE CASCADE,
  PRIMARY KEY (reviewId)
);
