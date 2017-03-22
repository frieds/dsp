import csv

# Q6.  Create a dictionary in the below format:
# faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              # 'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
# Print the first 3 key and value pairs of the dictionary:

professor = "Professor"
faculty_dict = {}
with open('faculty.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for faculty in reader:  # iterates through each row
        name = faculty[0]
        degree = faculty[1]
        index_space = name.rfind(" ")  # find last space in string
        last_name = name[index_space+1:]
        title_long_name = faculty[2]
        professor_index = title_long_name.find(professor)
        title = title_long_name[0:professor_index+len(professor)+1]
        email_address = faculty[3]
        faculty_info = [degree, title, email_address]
        if last_name not in faculty_dict:
            faculty_dict[last_name] = faculty_info
        else:
            if len(faculty_dict[last_name]) == 3:  # check if only one faculty_info entry per that last name
                faculty_dict[last_name] = [faculty_dict[last_name]]   # adds parentheses to make outer list
            faculty_dict[last_name].append(faculty_info)
    print("First 3 key:value pairs of the faculty_dict dictionary:")
    print({key: faculty_dict[key] for key in sorted(faculty_dict)[:3]})
# Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
# Print the first 3 key and value pairs of the dictionary:

professor_dict = {}
with open('faculty.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for faculty in reader:
        name = faculty[0]
        degree = faculty[1]
        index_space = name.rfind(" ")  # find last space in string
        last_name = name[index_space+1:]
        first_name = name[:index_space]
        title_long_name = faculty[2]
        professor_index = title_long_name.find(professor)
        title = title_long_name[0:professor_index+len(professor)+1]
        email_address = faculty[3]
        faculty_info = [degree, title, email_address]
        professor_dict[(first_name, last_name)] = faculty_info
    print("\n" + "The first three key:value pairs of professor_dict dictionary")
    print({key: professor_dict[key] for key in sorted(professor_dict)[:3]})


# Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based
#  on alphabetical orders of the last name of the professors

alphabetical_list = sorted(professor_dict.items(), key=lambda key: key[0][1])
print("\n" + "Print of previous dictionary key value pairs in a list format now based on alphabetical order of the last"
             " name of the professors" + "\n" + "{0}".format(alphabetical_list))

