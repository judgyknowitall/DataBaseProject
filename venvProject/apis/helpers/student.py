# Student Helper funtions


# Find a student by username
def get_student(sid):
    sqlCommand = 'SELECT * FROM student WHERE SUserName = %s;' % (sid)
    return  sqlCommand

# Create a new Mytutor student account 
def new_student(sid, name, psw):
    sqlCommand = 'INSERT INTO student Values(%s, %s, %s);' % (sid,name,psw)
    return sqlCommand

# Used to update an existing student
def edit_student(sid, name, psw):
    sqlCommand = 'UPDATE student SET SName = %s, SPassword = %s ' % (name, psw)
    sqlCommand += 'WHERE SUserName = %s;' % (sid)
    return sqlCommand

# Delete an existing Mytutor student account 
def delete_student(sid, psw):
    sqlCommand = 'DELETE FROM student WHERE SUserName = %s AND SPassword = %s;' % (sid,psw)
    return sqlCommand

