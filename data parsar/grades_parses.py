import pandas
import sqlite3


list_of_tuples = []
course_name = ""
course_number = ""
number_grades = ""
average_gpa = ""
a = ""
ab = ""
b = ""
bc = ""
c = ""
d = ""
f = ""
s = ""
u = ""
cr = ""
n = ""
p = ""
i = ""
nw = ""
nr = ""
other = ""

def connect():
    con = sqlite3.connect("data.db")
    return con

def close(con):
    con.commit()
    con.close()

def write_to_file(grades):
    with open("clean_data.txt", "a") as file:
        for elts in grades:
            file.write(str(elts))
            file.write(",")
        file.write('\n')
        file.close()
    #print(grades)

def parse_grade_info(cursor):
    files = ['fall17.txt', 'spring17.txt', 'fall16.txt', 'spring16.txt', 'fall15.txt', 'spring15.txt', 'fall14.txt']
    for curr_file in files:
        gradeDistributionDataCounter = 1
        with open (curr_file, "r") as myfile:
            data = myfile.readlines()
            curr_i = 0
            curr_dept = ""
            with open("clean_data.txt", "a") as file:
                file.write('^')
                file.write(curr_file[:len(curr_file)-4])
                file.write('\n')
                file.close()
            for global_counter in range(0, len(data)):
                #print(line)
                line = data[global_counter]
                if (line == "A AB B BC C D F S U CR N P I NW NR Other\n"):
                    curr_dept = data[curr_i+1]
                    #print("curr_dept" + curr_dept)
                    temp_curr = curr_i
                    for local_counter in range(global_counter + 1, len(data)):
                        inside_line = data[local_counter]
                        if (inside_line[0].isdigit()):
                            continue
                        elif "January" in inside_line:
                            break
                        elif "Summary" in inside_line:
                            break
                        elif "#" in inside_line:
                            break
                        #elif "A AB B BC C D" in inside_line:
                            #break
                        else:
                            #print(inside_line)
                            index_name = 0
                            for curr_char in str(inside_line):
                                #print(curr_char, end = ' ')
                                if curr_char.isdigit():
                                    break;
                                index_name += 1
                            #print("Length of inside_line = " + str(len(inside_line)) + "   index_name =  " + str(index_name))
                                    #print("STRANGE BEHAVIRO: " + curr_char + " " + str(index_name))
                            #print("index_name  = " + str(index_name))
                            if len(inside_line) > index_name and inside_line[index_name+1] == " " :
                                    index_name += 2
                            course_name = inside_line[0:index_name]
                            #print("course_name :" + course_name)
                            other_info = inside_line[index_name:len(inside_line)]
                            course_total_index = 0
                            for temp_char in str(other_info):
                                if temp_char.isdigit():
                                    break;
                                course_total_index += 1
                            other_info = other_info[course_total_index:len(other_info)]
                            other_info_arr = other_info.split()
                            #print("before parsing")
                            #print(other_info_arr)
                            #print(len(other_info_arr))
                            length = len(other_info_arr)
                            #Course Total Pass/Fail, No GPA
                            if length == 17:
                                num_index = 0
                                a_index = 1
                                ab_index = 2
                                b_index = 3
                                bc_index = 4
                                c_index = 5
                                d_index = 6
                                f_index = 7
                                s_index = 8
                                u_index = 9
                                cr_index = 10
                                n_index = 11
                                p_index = 12
                                i_index = 13
                                nw_index = 14
                                nr_index = 15
                                other_index = 16 
                                average_gpa = 0.0
                                grades = []

                                grades.append(curr_dept.rstrip())
                                prev_line = data[local_counter - 1]
                                temp_line = prev_line.split()
                                course_number = temp_line[0]
                                grades.append(course_number)
                                if other_info_arr[num_index] == '.':
                                    number_grades = 0
                                else:
                                    number_grades = other_info_arr[num_index]
                                grades.append(number_grades)

                                grades.append(average_gpa);

                                if other_info_arr[a_index] == '.':
                                    a = 0
                                else:
                                    a = other_info_arr[a_index]
                                grades.append(a)
                                if other_info_arr[ab_index] == '.':
                                    ab = 0
                                else:
                                    ab = other_info_arr[ab_index]
                                grades.append(ab)
                                if other_info_arr[b_index] == '.':
                                    b = 0
                                else:
                                    b = other_info_arr[b_index]
                                grades.append(b)
                                if other_info_arr[bc_index] == '.':
                                    bc = 0
                                else:
                                    bc = other_info_arr[bc_index]
                                grades.append(bc)
                                if other_info_arr[c_index] == '.':
                                    c = 0
                                else:
                                    c = other_info_arr[c_index]
                                grades.append(c)
                                if other_info_arr[d_index] == '.':
                                    d = 0
                                else:
                                    d = other_info_arr[d_index]
                                grades.append(d)
                                if other_info_arr[f_index] == '.':
                                    f = 0
                                else:
                                    f = other_info_arr[f_index]
                                grades.append(f)
                                if other_info_arr[s_index] == '.':
                                    s  = 0
                                else:
                                    s = other_info_arr[s_index]
                                grades.append(s)
                                if other_info_arr[u_index] == '.':
                                    u = 0
                                else:
                                    u = other_info_arr[u_index]
                                grades.append(u)
                                if other_info_arr[cr_index] == '.':
                                    cr = 0
                                else:
                                    cr = other_info_arr[cr_index]
                                grades.append(cr)
                                if other_info_arr[n_index] == '.':
                                    n  = 0
                                else:
                                    n = other_info_arr[n_index]
                                grades.append(n)
                                if other_info_arr[p_index] == '.':
                                    p = 0
                                else:
                                    p = other_info_arr[p_index]
                                grades.append(p)
                                if other_info_arr[i_index] == '.':
                                    i = 0
                                else:
                                    i = other_info_arr[i_index]
                                grades.append(i)
                                if other_info_arr[nw_index] == '.':
                                    nw  = 0
                                else:
                                    nw = other_info_arr[nw_index]
                                grades.append(nw)
                                if other_info_arr[nr_index] == '.':
                                    nr = 0
                                else:
                                    nr = other_info_arr[nr_index]
                                grades.append(nr)
                                if other_info_arr[other_index] == '.':
                                    other = 0
                                else:
                                    other = other_info_arr[other_index]
                                grades.append(other)
                                write_to_file(grades)
                                counter = 0
                                for grade in grades:   
                                    if (not isinstance(grades[counter], str)):
                                        grades[counter] = str(grades[counter])
                                    counter += 1
                                #query = "SELECT * FROM Course_Course WHERE courseDepartment LIKE" + "'%" + str(curr_dept.rstrip()) + "%'" + " AND courseNumber LIKE " + "'%" + str(course_number) + "%'"
                                # update course with foreign key of

                                #retval = cursor.execute("INSERT INTO Course_GradeDistributionData (numberGrades,averageGpa,a,ab,b,bc,c,d,f,s,u,cr,n,p,i,nw,nr,o) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", grades)
                                #print("INSERT INTOOOOOOOO
                                #print("INSERT INTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                #query = "UPDATE Course_Course SET gradeDistributionDataId_id = " + "'" + str(gradeDistributionDataCounter) + "'" + " WHERE courseDepartment LIKE" + "'%" + str(curr_dept.rstrip()) + "%'" + " AND courseNumber LIKE " + "'%" + str(course_number) + "%'"
                                #print (query)
                                #retval = cursor.execute(query)
                                gradeDistributionDataCounter += 1
                                
                            #Course Total GPA, GPA last element
                            elif length == 18:
                                num_index = 0
                                a_index = 1
                                ab_index = 2
                                b_index = 3
                                bc_index = 4
                                c_index = 5
                                d_index = 6
                                f_index = 7
                                s_index = 8
                                u_index = 9
                                cr_index = 10
                                n_index = 11
                                p_index = 12
                                i_index = 13
                                nw_index = 14
                                nr_index = 15
                                other_index = 16 
                                average_index = 17
                                average_gpa = 0.0
                                grades = []
                                grades.append(curr_dept.rstrip())

                                prev_line = data[local_counter - 1]
                                temp_line = prev_line.split()
                                course_number = temp_line[0]
                                grades.append(course_number)
                                if other_info_arr[num_index] == '.':
                                    number_grades = 0
                                else:
                                    number_grades = other_info_arr[num_index]
                                grades.append(number_grades)
                                if other_info_arr[average_index] == '.':
                                    average_gpa = 0.0
                                else:
                                    average_gpa = other_info_arr[average_index]
                                grades.append(average_gpa)
                                if other_info_arr[a_index] == '.':
                                    a = 0
                                else:
                                    a = other_info_arr[a_index]
                                grades.append(a)
                                if other_info_arr[ab_index] == '.':
                                    ab = 0
                                else:
                                    ab = other_info_arr[ab_index]
                                grades.append(ab)
                                if other_info_arr[b_index] == '.':
                                    b = 0
                                else:
                                    b = other_info_arr[b_index]
                                grades.append(b)
                                if other_info_arr[bc_index] == '.':
                                    bc = 0
                                else:
                                    bc = other_info_arr[bc_index]
                                grades.append(bc)
                                if other_info_arr[c_index] == '.':
                                    c = 0
                                else:
                                    c = other_info_arr[c_index]
                                grades.append(c)
                                if other_info_arr[d_index] == '.':
                                    d = 0
                                else:
                                    d = other_info_arr[d_index]
                                grades.append(d)
                                if other_info_arr[f_index] == '.':
                                    f = 0
                                else:
                                    f = other_info_arr[f_index]
                                grades.append(f)
                                if other_info_arr[s_index] == '.':
                                    s  = 0
                                else:
                                    s = other_info_arr[s_index]
                                grades.append(s)
                                if other_info_arr[u_index] == '.':
                                    u = 0
                                else:
                                    u = other_info_arr[u_index]
                                grades.append(u)
                                if other_info_arr[cr_index] == '.':
                                    cr = 0
                                else:
                                    cr = other_info_arr[cr_index]
                                grades.append(cr)
                                if other_info_arr[n_index] == '.':
                                    n  = 0
                                else:
                                    n = other_info_arr[n_index]
                                grades.append(n)
                                if other_info_arr[p_index] == '.':
                                    p = 0
                                else:
                                    p = other_info_arr[p_index]
                                grades.append(p)
                                if other_info_arr[i_index] == '.':
                                    i = 0
                                else:
                                    i = other_info_arr[i_index]
                                grades.append(i)
                                if other_info_arr[nw_index] == '.':
                                    nw  = 0
                                else:
                                    nw = other_info_arr[nw_index]
                                grades.append(nw)
                                if other_info_arr[nr_index] == '.':
                                    nr = 0
                                else:
                                    nr = other_info_arr[nr_index]
                                grades.append(nr)
                                if other_info_arr[other_index] == '.':
                                    other = 0
                                else:
                                    other = other_info_arr[other_index]
                                grades.append(other)
                                '''
                                print(curr_dept.rstrip())
                                print(course_name)
                                print(course_number)
                                '''
                                counter = 0
                                for grade in grades:   
                                    if (not isinstance(grades[counter], str)):
                                        grades[counter] = str(grades[counter])
                                    counter += 1
                                write_to_file(grades)
                                '''
                                retval = cursor.execute("INSERT INTO Course_GradeDistributionData (numberGrades,a,ab,b,bc,c,d,f,s,u,cr,n,p,i,nw,nr,o,averageGpa) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", grades)
                                print("INSERT INTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                query = "UPDATE Course_Course SET gradeDistributionDataId_id = " + "'" + str(gradeDistributionDataCounter) + "'" + " WHERE courseDepartment LIKE" + "'%" + str(curr_dept.rstrip()) + "%'" + " AND courseNumber LIKE " + "'%" + str(course_number) + "%'"
                                print (query)
                                retval = cursor.execute(query)
                                print(gradeDistributionDataCounter)
                                '''
                                gradeDistributionDataCounter += 1

                            #Single section Pass/Fail
                            elif length == 19:
                                course_num_index = 0
                                section_index = 1
                                num_index = 2
                                a_index = 3 
                                ab_index = 4 
                                b_index = 5 
                                bc_index = 6 
                                c_index = 7 
                                d_index = 8  
                                f_index = 9 
                                s_index = 10 
                                u_index = 11
                                cr_index = 12
                                n_index = 13
                                p_index = 14
                                i_index = 15
                                nw_index = 16
                                nr_index = 17
                                other_index = 18
                                average_gpa = 0.0

                                grades = []
                                grades.append(curr_dept.rstrip())

                                if other_info_arr[course_num_index] == '.':
                                    course_number = 0
                                else:
                                    course_number = other_info_arr[course_num_index]
                                grades.append(course_number)
                                if other_info_arr[section_index] == '.':
                                    section = 0
                                else:
                                    section = other_info_arr[section_index]
                                #grades.append(section)
                                if other_info_arr[num_index] == '.':
                                    number_grades = 0
                                else:
                                    number_grades = other_info_arr[num_index]
                                grades.append(number_grades)

                                grades.append(average_gpa) # for average gpa being missing due to pass fail course
                                if other_info_arr[a_index] == '.':
                                    a = 0
                                else:
                                    a = other_info_arr[a_index]
                                grades.append(a)
                                if other_info_arr[ab_index] == '.':
                                    ab = 0
                                else:
                                    ab = other_info_arr[ab_index]
                                grades.append(ab)
                                if other_info_arr[b_index] == '.':
                                    b = 0
                                else:
                                    b = other_info_arr[b_index]
                                grades.append(b)
                                if other_info_arr[bc_index] == '.':
                                    bc = 0
                                else:
                                    bc = other_info_arr[bc_index]
                                grades.append(bc)
                                if other_info_arr[c_index] == '.':
                                    c = 0
                                else:
                                    c = other_info_arr[c_index]
                                grades.append(c)
                                if other_info_arr[d_index] == '.':
                                    d = 0
                                else:
                                    d = other_info_arr[d_index]
                                grades.append(d)
                                if other_info_arr[f_index] == '.':
                                    f = 0
                                else:
                                    f = other_info_arr[f_index]
                                grades.append(f)
                                if other_info_arr[s_index] == '.':
                                    s  = 0
                                else:
                                    s = other_info_arr[s_index]
                                grades.append(s)
                                if other_info_arr[u_index] == '.':
                                    u = 0
                                else:
                                    u = other_info_arr[u_index]
                                grades.append(u)
                                if other_info_arr[cr_index] == '.':
                                    cr = 0
                                else:
                                    cr = other_info_arr[cr_index]
                                grades.append(cr)
                                if other_info_arr[n_index] == '.':
                                    n  = 0
                                else:
                                    n = other_info_arr[n_index]
                                grades.append(n)
                                if other_info_arr[p_index] == '.':
                                    p = 0
                                else:
                                    p = other_info_arr[p_index]
                                grades.append(p)
                                if other_info_arr[i_index] == '.':
                                    i = 0
                                else:
                                    i = other_info_arr[i_index]
                                grades.append(i)
                                if other_info_arr[nw_index] == '.':
                                    nw  = 0
                                else:
                                    nw = other_info_arr[nw_index]
                                grades.append(nw)
                                if other_info_arr[nr_index] == '.':
                                    nr = 0
                                else:
                                    nr = other_info_arr[nr_index]
                                grades.append(nr)
                                if other_info_arr[other_index] == '.':
                                    other = 0
                                else:
                                    other = other_info_arr[other_index]
                                grades.append(other)

                                '''
                                print(curr_dept.rstrip())
                                print(course_name)
                                print(course_number)
                                print(grades)
                                '''
                                counter = 0
                                for grade in grades:   
                                    if (not isinstance(grades[counter], str)):
                                        grades[counter] = str(grades[counter])
                                    counter += 1

                                write_to_file(grades)
                                '''
                                retval = cursor.execute("INSERT INTO Course_GradeDistributionData (numberGrades,a,ab,b,bc,c,d,f,s,u,cr,n,p,i,nw,nr,o,averageGpa) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", grades)
                                print("INSERT INTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                query = "UPDATE Course_Course SET gradeDistributionDataId_id = " + "'" + str(gradeDistributionDataCounter) + "'" + " WHERE courseDepartment LIKE" + "'%" + str(curr_dept.rstrip()) + "%'" + " AND courseNumber LIKE " + "'%" + str(course_number) + "%'"
                                print (query)
                                retval = cursor.execute(query)
                                print(gradeDistributionDataCounter)
                                '''
                                gradeDistributionDataCounter += 1

                            #Single section GPA
                            elif length == 20:
                                course_num_index = 0
                                section_index = 1
                                num_index = 2
                                average_index = 3
                                a_index = 4
                                ab_index = 5
                                b_index = 6
                                bc_index = 7
                                c_index = 8
                                d_index = 9
                                f_index = 10
                                s_index = 11
                                u_index = 12
                                cr_index = 13
                                n_index = 14
                                p_index = 15
                                i_index = 16
                                nw_index = 17
                                nr_index = 18
                                other_index = 19 
                                average_gpa = 0.0
                                grades = []
                                grades.append(curr_dept.rstrip())
                                if other_info_arr[course_num_index] == '.':
                                    course_number = 0
                                    grades.append(course_number)
                                else:
                                    course_number = other_info_arr[course_num_index]
                                    grades.append(course_number)
                                #grades.append(course_number)
                                if other_info_arr[section_index] == '.':
                                    section = 0
                                else:
                                    section = other_info_arr[section_index]
                                #grades.append(section)
                                if other_info_arr[num_index] == '.':
                                    number_grades = 0
                                else:
                                    number_grades = other_info_arr[num_index]
                                grades.append(number_grades)
                                if other_info_arr[average_index] == '.':
                                    average_gpa = 0
                                else:
                                    average_gpa = other_info_arr[average_index]
                                grades.append(average_gpa)
                                if other_info_arr[a_index] == '.':
                                    a = 0
                                else:
                                    a = other_info_arr[a_index]
                                grades.append(a)
                                if other_info_arr[ab_index] == '.':
                                    ab = 0
                                else:
                                    ab = other_info_arr[ab_index]
                                grades.append(ab)
                                if other_info_arr[b_index] == '.':
                                    b = 0
                                else:
                                    b = other_info_arr[b_index]
                                grades.append(b)
                                if other_info_arr[bc_index] == '.':
                                    bc = 0
                                else:
                                    bc = other_info_arr[bc_index]
                                grades.append(bc)
                                if other_info_arr[c_index] == '.':
                                    c = 0
                                else:
                                    c = other_info_arr[c_index]
                                grades.append(c)
                                if other_info_arr[d_index] == '.':
                                    d = 0
                                else:
                                    d = other_info_arr[d_index]
                                grades.append(d)
                                if other_info_arr[f_index] == '.':
                                    f = 0
                                else:
                                    f = other_info_arr[f_index]
                                grades.append(f)
                                if other_info_arr[s_index] == '.':
                                    s  = 0
                                else:
                                    s = other_info_arr[s_index]
                                grades.append(s)
                                if other_info_arr[u_index] == '.':
                                    u = 0
                                else:
                                    u = other_info_arr[u_index]
                                grades.append(u)
                                if other_info_arr[cr_index] == '.':
                                    cr = 0
                                else:
                                    cr = other_info_arr[cr_index]
                                grades.append(cr)
                                if other_info_arr[n_index] == '.':
                                    n  = 0
                                else:
                                    n = other_info_arr[n_index]
                                grades.append(n)
                                if other_info_arr[p_index] == '.':
                                    p = 0
                                else:
                                    p = other_info_arr[p_index]
                                grades.append(p)
                                if other_info_arr[i_index] == '.':
                                    i = 0
                                else:
                                    i = other_info_arr[i_index]
                                grades.append(i)
                                if other_info_arr[nw_index] == '.':
                                    nw  = 0
                                else:
                                    nw = other_info_arr[nw_index]
                                grades.append(nw)
                                if other_info_arr[nr_index] == '.':
                                    nr = 0
                                else:
                                    nr = other_info_arr[nr_index]
                                grades.append(nr)
                                if other_info_arr[other_index] == '.':
                                    other = 0
                                else:
                                    other = other_info_arr[other_index]
                                grades.append(other)
                                '''
                                print(curr_dept.rstrip())
                                print(course_name)
                                print(course_number)
                                '''
                                counter = 0
                                for grade in grades:   
                                    if (not isinstance(grades[counter], str)):
                                        grades[counter] = str(grades[counter])
                                    counter += 1

                                write_to_file(grades)
                                '''
                                retval = cursor.execute("INSERT INTO Course_GradeDistributionData (numberGrades,averageGpa,a,ab,b,bc,c,d,f,s,u,cr,n,p,i,nw,nr,o) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", grades)
                                print("INSERT INTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                query = "UPDATE Course_Course SET gradeDistributionDataId_id = " + "'" + str(gradeDistributionDataCounter) + "'" + " WHERE courseDepartment LIKE" + "'%" + str(curr_dept.rstrip()) + "%'" + " AND courseNumber LIKE " + "'%" + str(course_number) + "%'"
                                print (query)
                                retval = cursor.execute(query)
                                print(gradeDistributionDataCounter)
                                '''
                                gradeDistributionDataCounter += 1

                        temp_curr += 1
                curr_i+=1


if __name__ == "__main__":
    connection = connect()
    cursor = connection.cursor()
    parse_grade_info(cursor)
    close(connection)
