# Moderates Helper funtions


# Create a new moderates relation
def new_moderates(aid, sid, tid):
    sqlCommand = 'INSERT INTO moderates VALUES'
    sqlCommand+= '(%s, %s, %s);' % (aid, sid, tid)
    return sqlCommand

# Search for review moderator
def get_moderator(sid,tid):
    sqlCommand = 'SELECT AUserName FROM moderates WHERE '
    sqlCommand+= 'SUserName = %s AND TUserName = %s;' % (sid, tid)
    return sqlCommand

# Get all reviews moderated by an admin
def get_moderatedReview(aid):
    sqlCommand = 'SELECT * FROM review AS R, moderates AS M WHERE '
    sqlCommand+= 'R.SUserName = M.SUserName AND R.TUserName = M.TUserName AND '
    sqlCommand+= 'AUserName = %s;' % (aid)
    return sqlCommand