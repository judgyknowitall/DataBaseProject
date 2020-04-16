# TutorMeetsIn Helper funtions


# Get Tutors in location
def get_tutorsInLoc(pc=None, dist=None, city=None, country=None):

    sqlCommand = 'SELECT * FROM location, tutor_meets_in AS T '
    sqlCommand+= 'WHERE location.PostalCode = T.PostalCode'

    if country is not None:
        sqlCommand+= ' AND Country = %s' % (country)

        if city is not None:
            sqlCommand+= ' AND City = %s' % (city)

            if dist is not None:
                sqlCommand+= ' AND District = %s' % (dist)
    
    if pc is not None:
        sqlCommand+= ' AND location.PostalCode = %s' % (pc)

    sqlCommand+= ';'
    return sqlCommand

# Get location of a tutor
def get_locOfTutor(tid):

    sqlCommand = 'SELECT * FROM location, tutor_meets_in AS T '
    sqlCommand+= 'WHERE location.PostalCode = T.PostalCode '
    sqlCommand+= 'AND TUserName = %s;' % (tid)
    
    return sqlCommand

# Post a new tutorMeetsIn
def new_tutorMeetsIn(tid, pc):
    sqlCommand = 'INSERT INTO tutor_meets_in VALUES'
    sqlCommand+= '(%s, %s);' % (tid, pc)
    return sqlCommand

# Delete an existing tutorMeetsIn
def delete_tutorMeetsIn(tid, pc):
    sqlCommand = 'DELETE FROM tutor_meets_in WHERE '
    sqlCommand+= 'TUserName = %s AND PostalCode = %s;' % (tid,pc)
    return sqlCommand
