# Tutor Helper funtions


# Used to get the list of all tutors 
def getAll_tutor():
    sqlCommand = 'SELECT * FROM tutor;'
    return  sqlCommand

# Find all tutors for a specific subject
def getExpert_tutor(subject):
    sqlCommand = 'SELECT * FROM tutor, tutor_subject_expertise AS E WHERE '
    sqlCommand+= 'tutor.TUserName = E.TUserName AND SubjectExpertise = %s;' % (subject)
    return  sqlCommand

# Used to create a new tutor account 
def new_tutor(tid, name, psw, bg):
    sqlCommand = 'INSERT INTO tutor Values'
    sqlCommand+= '(%s, %s, %s, %s, Null, FALSE, FALSE, 0);' % (tid,name,psw,bg)
    return sqlCommand

# Get all details of a specific tutor 
def get_tutor(tid):
    sqlCommand = 'SELECT * FROM tutor WHERE TUserName = %s;' % (tid)
    return  sqlCommand

# Edit a specific tutor account 
def edit_tutor(tid, name, psw, bg):
    sqlCommand = 'UPDATE tutor SET TName = %s, TPassword = %s, Background = %s' % (name, psw, bg)
    sqlCommand += ' WHERE TUserName = %s;' % (tid)
    return sqlCommand

# Modify the tutor’s police check and approval result
def approve_tutor(tid, aid, police, rslt):
    sqlCommand = 'UPDATE tutor SET AUserName = %s, Result = %s, PoliceCheck = %s' % (aid, rslt, police)
    sqlCommand += ' WHERE TUserName = %s;' % (tid)
    return sqlCommand

# Used to delete a specific tutor account  
def delete_tutor(tid, psw):
    sqlCommand = 'DELETE FROM tutor WHERE TUserName = %s AND TPassword = %s;' % (tid,psw)
    return sqlCommand