import csv

# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# probably best to create a new dictionary with the name of the team and that difference value
# then you can find the max in that dictionary and simply print the name of the key

with open('football.csv') as csv_file:
    football_dict = {}
    reader = csv.reader(csv_file)
    next(reader)  # skips the header row in football.csv
    for row in reader:
        absolute_goals_difference = abs(int(row[5]) - int(row[6]))
        football_dict[row[0]] = absolute_goals_difference
    team_smallest_goal_difference = min(football_dict, key=football_dict.get)
    print(team_smallest_goal_difference)
