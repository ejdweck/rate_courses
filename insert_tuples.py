import pandas
import sqlite3
import datetime

userIdList = []

def connect():
    con = sqlite3.connect("data.db")
    return con

def close(con):
    con.commit()
    con.close()

def insert_tuples(cursor):
    #insert instructor
    query = "INSERT OR IGNORE INTO Instructor (instructorId,firstName,lastName) VALUES (1,'Adel','Ardelan')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Instructor (instructorId,firstName,lastName) VALUES (2,'Colin','Engstrom')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Instructor (instructorId,firstName,lastName) VALUES (3,'Jin-Yi','Cai')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Instructor (instructorId,firstName,lastName) VALUES (4,'Beck','Hasti')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Instructor (instructorId,firstName,lastName) VALUES (5,'Andrea','Arpaci-Dusseau')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Instructor (instructorId,firstName,lastName) VALUES (6,'Tracy','Lewis-Williams')"
    cursor.execute(query)

    #insert courses
    query = "INSERT OR IGNORE INTO Course (courseName,courseNumber,courseDepartment,averageRating) VALUES ('Databases','564','CS',1.0)"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseName,courseNumber,courseDepartment,averageRating) VALUES ('Artificial Intelligence','540','CS',2.0)"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseName,courseNumber,courseDepartment,averageRating) VALUES ('Algorithims','577','CS',3.0)"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseName,courseNumber,courseDepartment,averageRating) VALUES ('Discrete Math','240','CS',4.0)"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseName,courseNumber,courseDepartment,averageRating) VALUES ('Operating Systems','537','CS',5.0)"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseName,courseNumber,courseDepartment,averageRating) VALUES ('Human Computer Interaction','570','CS',6.0)"
    cursor.execute(query)

    #insert courseReviews
    query = "INSERT OR IGNORE INTO CourseReview (courseDepartment,courseNumber,reviewId,instructorId,review,reviewerId,rating,reviewDate) VALUES ('CS','564',1,1,'This course was quite difficult. Do not take concurrently with another programming course!',1,5,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (courseDepartment,courseNumber,reviewId,instructorId,review,reviewerId,rating,reviewDate) VALUES ('CS','540',2,2,'Easy class. Take and cruise through dudes.',1,6,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (courseDepartment,courseNumber,reviewId,instructorId,review,reviewerId,rating,reviewDate) VALUES ('CS','577',3,3,'Godspeed, brother.',1,6,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (courseDepartment,courseNumber,reviewId,instructorId,review,reviewerId,rating,reviewDate) VALUES ('CS','240',4,4,'Challenging concepts but doable with enough effort. Make sure you take with the CS department.',1,7,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (courseDepartment,courseNumber,reviewId,instructorId,review,reviewerId,rating,reviewDate) VALUES ('CS','537',5,5,'One of the better courses at in this department but really a bear. Lots of C programming.',1,4,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (courseDepartment,courseNumber,reviewId,instructorId,review,reviewerId,rating,reviewDate) VALUES ('CS','570',6,6,'GPA boosting CS elective lol',1,9,'')"
    cursor.execute(query)

if __name__ == "__main__":
    connection = connect()
    cursor = connection.cursor()
    insert_tuples(cursor)
    close(connection)
