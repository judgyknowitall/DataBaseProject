# Location Helper funtions


# Create new location in database
def new_location(pc, dist, city, country=None):
    sqlCommand = 'INSERT INTO location'

    if country is None:
        sqlCommand+= '(PostalCode, District, City) VALUES'
        sqlCommand+= '(%s, %s, %s);' % (pc, dist, city)
    else:
        sqlCommand+= ' VALUES(%s, %s, %s, %s);' % (pc, dist, city, country)
    
    return sqlCommand

# Find locations
def get_location(dist=None, city=None, country=None):

    sqlCommand = 'SELECT * FROM location'

    if country is not None:
        sqlCommand+= ' WHERE Country = %s' % (country)

        if city is not None:
            sqlCommand+= ' AND City = %s' % (city)

            if dist is not None:
                sqlCommand+= ' AND District = %s' % (dist)

    sqlCommand+= ';'
    return sqlCommand
