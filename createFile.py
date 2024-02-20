import csv

# Define the data to be written into the CSV file
data = [
    ['Name', 'Age', 'Occupation'],
    ['John Doe', '28', 'Software Engineer'],
    ['Jane Doe', '32', 'Data Scientist'],
    ['Jim Brown', '45', 'Manager']
]

# Specify the name of the CSV file to be created
filename = 'people.csv'

# Open the file in write mode ('w') and create a csv.writer object
# newline='' is used to prevent blank rows in the output on Windows
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    writer.writerows(data)

print(f'CSV file "{filename}" has been created successfully.')
