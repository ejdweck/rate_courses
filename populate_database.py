import os, random, datetime

courses = []


def populate():
    add_instructor("Kristaps", "Porzingis")
    add_instructor("Lebron", "James")
    add_instructor("Kyrie", "Irving")
    add_instructor("John", "Wall")
    # Print out what we have added to the user.
    for c in Instructor.objects.all():
        print(c.firstName)


    # read courses from a file and compile into a list
    #all_courses = read_course_data()
    all_courses = []
    # add courses to db from list
    course_count = 1 
    for course in all_courses:
        # create grade distribution object null and add to course (will fill later)
        # i think every 
        

        # split all cross listed courses into individual courses
        cross_listed = course[1].split("/")
        if len(cross_listed) > 1:
            for c in cross_listed:
                grade_distro_semester = add_grade_distribution_semester(
                    gradeDistributionSemesterId=course_count,
                    fall17=None,
                    spring17=None,
                    fall16=None,
                    spring16=None,
                    fall15=None,
                    spring15=None,
                    fall14=None,
                )
                add_course(c.rstrip(),course[2],course[0],0,0,course[4],course[3],grade_distro_semester)
        else:
            grade_distro_semester = add_grade_distribution_semester(
                gradeDistributionSemesterId=course_count,
                fall17=None,
                spring17=None,
                fall16=None,
                spring16=None,
                fall15=None,
                spring15=None,
                fall14=None,
            )
            print (grade_distro_semester.gradeDistributionSemesterId)
            # add each course to the db
            add_course(course[1].rstrip(),course[2],course[0],0,0,course[4],course[3],grade_distro_semester)
        course_count += 1

    #read_grade_distribution_data()
    add_course_tags()
    add_fake_course_reviews()

def add_course_tags():
    for i in range(4):
        tag = add_course_review_tags(random.randint(1,4), random.randint(1,4), random.randint(1,4), random.randint(1,4))

def add_fake_course_reviews():
    all_courses = Course.objects.all() 
    for c in all_courses:
        for x in range(5):
            review_text = "It's a dangerous business, Frodo, going out your door. You step onto the road, and if you don't keep your feet, there's no knowing where you might be swept off to."
            tag = CourseReviewTag.objects.get(courseReviewTagId=random.randint(1,4))
            instructor = Instructor.objects.get(instructorId=random.randint(1,4))
            review = add_course_review(c,instructor,tag,review_text, random.randint(1,10), datetime.datetime.now())

def read_grade_distribution_data():
    curr_course_dept = ""
    curr_semester = ""
    file = open("clean_data.txt","r")
    for line in file: 
        if (line[0] == "^"):
            curr_semester = line[1:].rstrip()
            print(curr_semester)
            line = next(file)
        else:
            course_data = line.split(",")
            curr_course_dept = course_data[0]
            curr_course_num = course_data[1]
            grade_distro_data = add_grade_distribution_data(
                course_data[2],
                course_data[3],
                course_data[4],
                course_data[5],
                course_data[6],
                course_data[7],
                course_data[8],
                course_data[9],
                course_data[10],
                course_data[11],
                course_data[12],
                course_data[13],
                course_data[14],
                course_data[15],
                course_data[16],
                course_data[17],
                course_data[18],
                course_data[19],
            )

            # find the appropriate course object
            try:
                print(curr_course_dept + str("whitespacetest"))
                print(curr_course_num)
                curr_course = Course.objects.get(courseDepartment=curr_course_dept, courseNumber=curr_course_num)
            except:
                print("EXCEPTIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

            # fill course object with foreign key depending on semester

            if curr_semester == "fall17":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.fall17 = grade_distro_data
                print(grade_distro_sem.fall17)
                grade_distro_sem.save()

            elif curr_semester == "spring17":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.spring17 = grade_distro_data
                print(grade_distro_sem.spring17)
                grade_distro_sem.save()

            elif curr_semester == "fall16":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.fall16 = grade_distro_data
                print(grade_distro_sem.fall16)
                grade_distro_sem.save()

            elif curr_semester == "spring16":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.spring16 = grade_distro_data
                print(grade_distro_sem.spring16)
                grade_distro_sem.save()
                
            elif curr_semester == "fall15":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.fall15 = grade_distro_data
                print(grade_distro_sem.fall15)
                grade_distro_sem.save()
                
                
            elif curr_semester == "spring15":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.spring15 = grade_distro_data
                print(grade_distro_sem.spring15)
                grade_distro_sem.save()
                
            elif curr_semester == "fall14":
                grade_distro_sem = curr_course.gradeDistributionSemesterId
                grade_distro_sem.fall14 = grade_distro_data
                print(grade_distro_sem.fall14)
                grade_distro_sem.save()
                
def read_course_data():
    query = ''
    file_ = open('course_data.txt', 'r', encoding="utf-8")
    for line in file_:
        temp = str(line)
        #print(temp)
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

        course = []
        course.append(course_name)
        course.append(course_dept)
        course.append(course_num)
        course.append(course_info)
        course.append(credits)
        courses.append(course)
    return courses;

def add_instructor(firstname, lastname):
    instructor = Instructor.objects.get_or_create(firstName=firstname, lastName=lastname)[0]
    return instructor

def add_course(courseDepartment, courseNumber, courseName, averageRating, numberOfRatings, credits, courseInfo, gradeDistributionSemesterId):
    course = Course.objects.get_or_create(
        courseDepartment=courseDepartment,
        courseNumber=courseNumber,
        courseName=courseName,
        averageRating=averageRating,
        numberOfRatings=numberOfRatings,
        credits=credits,
        courseInfo=courseInfo,
        gradeDistributionSemesterId=gradeDistributionSemesterId
    )[0]
    print(course.courseDepartment)
    return course

def add_course_review_tags(weedOutCourse, interestingContent, lotsOfHomework, mandatoryAttendance):
    courseReviewTag = CourseReviewTag.objects.get_or_create(
        weedOutCourse=weedOutCourse,
        interestingContent=interestingContent,
        lotsOfHomework=lotsOfHomework,
        mandatoryAttendance=mandatoryAttendance
    )[0]
    return courseReviewTag

def add_course_review(courseId, instructorId, courseReviewTagId, review, rating, reviewDate):
    courseReview = CourseReview.objects.get_or_create(
        courseId=courseId,
        instructorId=instructorId,
        courseReviewTagId=courseReviewTagId,
        review=review,
        rating=rating,
        reviewDate=reviewDate
    )[0]
    return courseReview

def add_grade_distribution_data(numberGrades, averageGpa, a, ab, b, bc, c, d, f, s, u, cr, n, p, i, nw, nr, o):
    grade_distribution_data = GradeDistributionData.objects.get_or_create(
        numberGrades=numberGrades, 
        averageGpa=averageGpa,
        a=a, 
        ab=ab,
        b=b,
        bc=bc,
        c=c, 
        d=d,
        f=f,
        s=s,
        u=u,
        cr=cr,
        n=n,
        p=p,
        i=i,
        nw=nw,
        nr=nr,
        o=o
    )[0]
    return grade_distribution_data

def add_grade_distribution_semester(gradeDistributionSemesterId, fall17, spring17, fall16, spring16, fall15, spring15, fall14):
    grade_distribution_semester = GradeDistributionSemester.objects.get_or_create (
        gradeDistributionSemesterId=gradeDistributionSemesterId,
        fall17=fall17,
        spring17=spring17,
        fall16=fall16,
        spring16=spring16,
        fall15=fall15,
        spring15=spring15,
        fall14=fall14
    )[0]
    return grade_distribution_semester

# Start execution here!
if __name__ == '__main__':
    print ("Starting db population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_courses.settings')
    import django
    django.setup()
    from course.models import Course, Instructor, CourseReview, CourseReviewTag, GradeDistributionSemester, GradeDistributionData
    populate()