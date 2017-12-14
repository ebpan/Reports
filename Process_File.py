class process:

    def process_file(self, input_file, output_file):
        # start reading the input file from the second line in order to skip headers
        lines = input_file.readlines()[1:]
        # print(lines)
        output_file.write("EMPLID" + "," + "LAST_NAME" + "," + "FIRST_NAME" + "," + "EMAIL1" + "," + "EMAIL2" + "," + "SIS_ID" + "," + "USERNAME" + "," + "AUTH_DATE" + "," + "ROLES" + "\n")
        # for each line in the file
        for line in lines:
            # print(line)

            # break up the line by the | character into separate variables, with all the roles that are comma separated being stored under 'roles'
            emplid, last, first, empl_email, stu_email, SIS_ID, username, auth_date, roles = line.split("|")


            rolesList = []
            i = 0
            for role in roles.split(","):
                rolesList.append(role)

            # print(rolesList[1])
            last_record = len(rolesList) - 1
            del rolesList[last_record]

            while i < len(rolesList):
                print(
                    emplid + "," + last + "," + first + "," + empl_email + "," + stu_email + "," + SIS_ID + "," + username + "," + auth_date + "," +
                    rolesList[i])
                output_file.write(
                    emplid + "," + last + "," + first + "," + empl_email + "," + stu_email + "," + SIS_ID + "," + username + "," + auth_date + "," +
                    rolesList[i] + "\n")
                i = i + 1