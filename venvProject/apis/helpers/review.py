# Review Helper funtions

# Used to get all reviews of a tutor 
def get_reviewByTID(tid):
    sqlCommand = 'SELECT * FROM review WHERE TUserName = %s;' % (tid)
    return sqlCommand

# Create a new review 
def new_review(tid, sid, rating, comment):
    sqlCommand = 'INSERT INTO review VALUES'
    sqlCommand+= '(%s, %s, %s, %s, NULL);' % (tid, sid, rating, comment)
    return sqlCommand

# Edit an existing review 
def edit_review(tid, sid, rating, comment): 
    sqlCommand = 'UPDATE review SET Rating = %s, Comment = %s ' % (rating, comment)
    sqlCommand+= 'WHERE TUserName = %s AND SUserName = %s' % (tid, sid)
    return sqlCommand

# Edit accuracy of existing review
def edit_reviewAcc(tid, sid, acc): 
    sqlCommand = 'UPDATE review SET  Accuracy = %s ' % (acc)
    sqlCommand+= 'WHERE TUserName = %s AND SUserName = %s' % (tid, sid)
    return sqlCommand

# Delete and existing review 
def delete_review(tid, sid):
    sqlCommand = 'DELETE FROM review '
    sqlCommand+= 'WHERE TUserName = %s AND SUserName = %s' % (tid, sid)
    return sqlCommand