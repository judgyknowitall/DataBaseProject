# Function to setup database connection
# Prompt user for a database connection


import os,os.path

# Main function
def main():

    # Prompt user for connection variables
    host = input("Please input host(eg. localhost): ")
    user = input("Please input server username(eg. root): ")
    psw = input("Please input server password(eg. database.W2020): ")

    # Write inputs to file
    path = os.path.join(os.getcwd(),"apis/db_connect")
    fd = open("%s/db.txt"%(path),'w')
    fd.write("%s\n%s\n%s\nmytutor" % (host, user, psw))
    fd.close()

    print("Database connection variables successfully stored in:")
    print(path)


# Run main
main()