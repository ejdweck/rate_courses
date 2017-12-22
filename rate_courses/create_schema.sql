DROP TABLE Course;
CREATE TABLE Course (
  courseId VARCHAR(30) NOT NULL,
  courseName VARCHAR(30) NOT NULL,
  courseNumber VARCHAR(30) NOT NULL,
  PRIMARY KEY (courseId)
);

DROP TABLE CourseReview;
CREATE TABLE CourseReview (
  reviewId VARCHAR(30) NOT NULL,
  courseId VARCHAR(30) NOT NULL,
  professor VARCHAR(30) NOT NULL,
  review VARCHAR(30) NOT NULL,
  reviewDate DATE NOT NULL,
  PRIMARY KEY (reviewId),
  FOREIGN KEY (courseId) REFERENCES Course(courseId)
  ON DELETE CASCADE
);
