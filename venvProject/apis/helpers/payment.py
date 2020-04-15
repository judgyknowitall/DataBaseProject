# Payment Helper funtions

# returns all current payments
def getAll_payments():
    sqlCommand = 'SELECT * FROM payment'
    return sqlCommand

# Used to create a new payment 
def new_payment(amount, sid, tid, first=False):

    # Not 1st item in payment table
    if not first:
        sqlCommand = 'INSERT INTO payment(Amount, SUserName, TUserName) Values'
        sqlCommand+= '(%s,%s,%s)' % (amount, sid, tid)

    # 1st item in payment table
    else:
        sqlCommand = 'INSERT INTO payment Values'
        sqlCommand+= '(1, %s, CURRENT_TIMESTAMP, %s, %s)' % (amount, sid, tid)

    return sqlCommand

# Used to get all the payments made to a specific tutor past a certain date
def get_paymentsToTutor(tid, date):
    sqlCommand = 'SELECT * FROM payment WHERE '
    sqlCommand+= 'TUserName = %s AND DATE(PaymentDate) >= %s' % (tid, date)
    return sqlCommand

# Used to get all the payments made by a specific student past a certain date
def get_paymentsFromStudent(sid, date):
    sqlCommand = 'SELECT * FROM payment WHERE '
    sqlCommand+= 'SUserName = %s AND DATE(PaymentDate) >= %s' % (sid, date)
    return sqlCommand

# Used to get all the payments made by a specific student to a tutor past a certain date
def get_paymentsFromSToT(sid, tid, date):
    sqlCommand = 'SELECT * FROM payment WHERE '
    sqlCommand+= 'SUserName = %s AND TUserName = %s AND DATE(PaymentDate) >= %s' % (sid, tid, date)
    return sqlCommand