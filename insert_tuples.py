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
    #insert courses
    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES ('1','Databases','CS564')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES ('2','Artificial Intelligence','CS540')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES ('3','Algorithims','CS577')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES ('4','Discrete Math','CS240')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES ('5','Operating Systems','CS537')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO Course (courseId,courseName,courseNumber) VALUES ('6','Human Computer Interaction','CS570')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professor,review,reviewDate) VALUES ('1','1','Adel Ardalan','This course was quite difficult. Do not take concurrently with another programming course!', '')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professor,review,reviewDate) VALUES ('2','2','Colin Engstrom','Easy class. Take and cruise through dudes.', '')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professor,review,reviewDate) VALUES ('3','3','Jin Cai-Yi','Godspeed, brother.', '')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professor,review,reviewDate) VALUES ('4','4','Beck Hasti','Challenging concepts but doable with enough effort. Make sure you take with the CS department.', '')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professor,review,reviewDate) VALUES ('5','5','Andrea Arpaci-Dusseau','One of the better courses at in this department but really a bear. Lots of C programming.','')"
    cursor.execute(query)

    query = "INSERT OR IGNORE INTO CourseReview (reviewId,courseId,professor,review,reviewDate) VALUES ('6','6','Tracy Lewis-Williams','GPA boosting CS elective lol', '')"
    cursor.execute(query)

if __name__ == "__main__":
    connection = connect()
    cursor = connection.cursor()
    insert_tuples(cursor)
    close(connection)
