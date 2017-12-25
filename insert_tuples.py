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
    #insert professors
    query = "INSERT OR IGNORE INTO Professor (professorId,firstName,lastName) VALUES (1,'Adel','Ardelan')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Professor (professorId,firstName,lastName) VALUES (2,'Colin','Engstrom')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Professor (professorId,firstName,lastName) VALUES (3,'Jin-Yi','Cai')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Professor (professorId,firstName,lastName) VALUES (4,'Beck','Hasti')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Professor (professorId,firstName,lastName) VALUES (5,'Andrea','Arpaci-Dusseau')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Professor (professorId,firstName,lastName) VALUES (6,'Tracy','Lewis-Williams')"
    cursor.execute(query)



    #insert courses
    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES (1,'Databases','CS564')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES (2,'Artificial Intelligence','CS540')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES (3,'Algorithims','CS577')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES (4,'Discrete Math','CS240')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES (5,'Operating Systems','CS537')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES (6,'Human Computer Interaction','CS570')"
    cursor.execute(query)

    #insert courseReviews
    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professorId,review,rating,reviewDate) VALUES (1,1,1,'This course was quite difficult. Do not take concurrently with another programming course!',5, '')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professorId,review,rating,reviewDate) VALUES (2,2,2,'Easy class. Take and cruise through dudes.',6,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professorId,review,rating,reviewDate) VALUES (3,3,3,'Godspeed, brother.',6,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professorId,review,rating,reviewDate) VALUES (4,4,4,'Challenging concepts but doable with enough effort. Make sure you take with the CS department.',7,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professorId,review,rating,reviewDate) VALUES (5,5,5,'One of the better courses at in this department but really a bear. Lots of C programming.',4,'')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professorId,review,rating,reviewDate) VALUES (6,6,6,'GPA boosting CS elective lol',9,'')"
    cursor.execute(query)

if __name__ == "__main__":
    connection = connect()
    cursor = connection.cursor()
    insert_tuples(cursor)
    close(connection)
