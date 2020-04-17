# Tutor Subject Expertise Helper function


# Get the subject expertise of a tutor
def get_subjExp(tid):
    sqlCommand = 'SELECT SubjectExpertise FROM tutor_subject_expertise WHERE '
    sqlCommand+= 'TUserName = %s;' % (tid)
    return sqlCommand

# Create a new subject expertise for a tutor
def new_subjExp(tid, subj):
    sqlCommand = 'INSERT INTO tutor_subject_expertise VALUES'
    sqlCommand+= '(%s, %s)' % (tid, subj)
    return sqlCommand

# Search for tutors with subject expertise
def get_tutorsPerSubjExp(subj):
    sqlCommand = 'SELECT TUserName FROM tutor_subject_expertise WHERE '
    sqlCommand+= 'SubjectExpertise = %s;' % (subj)
    return sqlCommand

# Can either delete by a tutor id only, deleting all rows with them, or one specific row with all fields specified
def delete_subjExp(tid,subj):
    if subj == "":
        return "DELETE FROM tutor_subject_expertise WHERE TUserName=%s;" % (tid,)
    else:
        return "DELETE FROM tutor_subject_expertise WHERE TUserName=%s AND SubjectExpertise=%s;" % (tid,subj,)