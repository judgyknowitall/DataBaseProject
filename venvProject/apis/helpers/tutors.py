# Tutors Helper funtions


# Get all tutors relationships
def getAll_tutors():
    sqlCommand = 'SELECT * FROM tutors;'
    return sqlCommand

# Get tutors relationships for a specific tutor
def get_tutorsTutor(tid):
    sqlCommand = 'SELECT * FROM tutors WHERE '
    sqlCommand+= 'TUserName = %s;' % (tid)
    return sqlCommand

# Get tutors relationship for a specific student
def get_tutorsStudent(sid):
    sqlCommand = 'SELECT * FROM tutors WHERE '
    sqlCommand+= 'SUserName = %s;' % (sid)
    return sqlCommand

# Create a new tutors relationship
def new_tutors(tid, sid, start, first=False):

    # Not 1st item in payment table
    if not first:
        sqlCommand = 'INSERT INTO tutors(TUserName, SUserName, StartDate, EndDate) '
        sqlCommand+= 'VALUES(%s, %s, %s, NULL)' % (tid, sid, start)
        return sqlCommand
    
    # 1st item in payment table
    else:
        sqlCommand = 'INSERT INTO tutors VALUES'
        sqlCommand+= '(1, %s, %s, %s, NULL);' % (tid, sid, start)
        return sqlCommand

# Add an end date to an existing tutors relationship
def end_tutors(tutId, end):
    sqlCommand = 'UPDATE tutors SET EndDate = %s ' % (end)
    sqlCommand+= 'WHERE Tutoring_id = %s;' % (tutId)
    return sqlCommand

# Delete an existing tutors relationship
def delete_tutors(tutId):
    sqlCommand = 'DELETE FROM tutors WHERE Tutoring_id = %s;' % (tutId)
    return sqlCommand