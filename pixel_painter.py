# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 11.2
# Date: 11/13/2023

OpenFile = input("Enter the filename: ")


# Split filename to extract base name (excluding extension)
FileN = OpenFile.split('.')
newName = FileN[0] + ".txt"


# Open text file to write answers into
f = open(newName, 'w')


# Open the input file for reading
with open(OpenFile, 'r') as input_file:
    # Prompt the user for a character to use
    character = input("Enter a character: ")


    # Iterate through each line in the input file
    for row in input_file:
        # Split the line by commas and remove leading/trailing whitespace
        nums = row.strip().split(',')
        answers = []


        # Process each number in the line
        for index, number in enumerate(nums):
            number = int(number)
            if index % 2 == 0:   
                answers.append(' ' * number)
            else:
                answers.append(character * number)


        # Combine the results into a single string
        resultStr = ''.join(answers)


        # Write the result to the new text file
        f.write(f"{resultStr}\n")


# Close the input file and the new text file
f.close()


# Display a message indicating the new file has been created
print(f"{newName} created!")
