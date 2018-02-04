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

    query = ''
    file_ = open('new_data.txt', 'r', encoding="utf-8")

    for line in file_:
        temp = str(line)
        print(temp)
        init_split = temp.split(' — ')
        next_split = init_split[1].split('%')
        course_name = next_split[0]
        last_split = next_split[1].split('^')
        course_info = last_split[1]
        credits = last_split[0][0:len(last_split[0])-8]
        num_index = 0
        for c in range(0,len(init_split[0])):
            if init_split[0][c].isdigit():
                num_index = c
                break
        course_dept = init_split[0][0:num_index]
        course_num = init_split[0][num_index:len(init_split[0])]
        values = (course_dept, course_num, course_name, 0, 0, course_info, credits)
        print(values)
        cursor.execute("INSERT INTO Course_Course (courseDepartment,courseNumber,courseName, averageRating, numberOfRatings, courseInfo, credits) VALUES (?,?,?,?,?,?,?)", values)

if __name__ == "__main__":
    connection = connect()
    cursor = connection.cursor()
    insert_tuples(cursor)
    close(connection)
