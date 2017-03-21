import csv

# Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

degrees_frequencies = {}
with open('faculty.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for faculty in reader:
        degrees = faculty[1]
        degree_no_period = degrees.replace(".", '')
        new_degree_list = degree_no_period.split()  # splits by spaces between titles
        while new_degree_list:
            degree = new_degree_list.pop()
            if len(degree) >= 2:
                if degree not in degrees_frequencies:
                    degrees_frequencies[degree] = 1
                else:
                    degrees_frequencies[degree] += 1
    print("The unique degrees and their frequencies are: {0}".format(degrees_frequencies))
    print("The number of unique degrees is: {0}".format(degrees_frequencies))

# Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

title_frequencies = {}
with open('faculty.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for faculty in reader:
        title = faculty[2]
        title = title.replace(' is ', ' of ')
        if title not in title_frequencies:
            title_frequencies[title] = 1
        else:
            title_frequencies[title] += 1
    print("The titles of the faculty and their frequencies: {0}".format(title_frequencies))
    print("The number of unique titles of faculty: {0}".format(len(title_frequencies)))

# Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

faculty_email_addresses = []
with open('faculty.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for faculty in reader:
        email_address = faculty[3]
        faculty_email_addresses.append(email_address)
    print("List of faculty email addresses: {0}".format(faculty_email_addresses))


# Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).
# Print the list of unique email domains.

email_domains = []
for email in faculty_email_addresses:
    at_symbol_index = email.find("@")
    email_domain = email[at_symbol_index+1:]
    email_domains.append(email_domain)
unique_email_domains = set(email_domains)
number_of_unique_domains = len(set(email_domains))
print("Number of unique email domains: {0}".format(number_of_unique_domains))
print("Set of unique email domains: {0}".format(unique_email_domains))
