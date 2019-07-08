def ValidateUser(user, passwd) :
    retval = False
    role = "Invalid"
    with open("user.dat", "r") as filestream:
        users = []
        for line in filestream:
            row =[]
            fields = line.split(",")
            row.append(fields[0])
            row.append(fields[1])
            row.append(fields[2])
            users.append(row)
    print(users)
    for row in users:
        login = row[0]
        password =  row[1]
        if user == login:
           if passwd == password:
              retval = True
              role  = row[2]
              break
    return retval,role


result, role = ValidateUser('flooradmin', '2522')
print(result, " " , role)
