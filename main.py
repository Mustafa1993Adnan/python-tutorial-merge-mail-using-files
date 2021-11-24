# TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as starting_letter:
    orginal_letter = starting_letter.read()
with open("Input/Names/invited_names.txt") as invited_names:
    while invited_person := invited_names.readline().rstrip():
        letter = orginal_letter.replace('[name]', f"{invited_person}")
        with open(f"Output/ReadyToSend/letter_for_{invited_person}.txt", mode='w') as output_file:
            output_file.write(letter)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
