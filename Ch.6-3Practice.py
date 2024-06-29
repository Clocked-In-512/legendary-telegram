##Robert Fernandez
##Complete
##This program will display the student's name, and their final exam score in a table.



# Open the file for reading
with open('students.txt', 'r') as file:
    
    # Print the header
    print('Name                Score')
    print('--------------------------------')
    
    # Loop through each line in the file
    for line in file:
        
        # Strip any extra newline or spaces and split the line into words
        name, score = line.strip().split(',')
        
        # Print the name and score
        print(f'{name:<20} {score}')
