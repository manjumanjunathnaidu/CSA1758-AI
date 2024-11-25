import itertools

# Function to solve a cryptarithm
def solve_cryptarithm():
    # Define the letters involved in the cryptarithm
    letters = 'MOONSOONJUNE'
    
    # Get all unique letters
    unique_letters = ''.join(set(letters))
    
    # Ensure there are no more than 10 unique letters (since there are only 10 digits)
    if len(unique_letters) > 10:
        return "Too many unique letters"
    
    # Generate all permutations of digits for the unique letters
    for perm in itertools.permutations(range(10), len(unique_letters)):
        # Create a mapping of letters to digits
        letter_to_digit = dict(zip(unique_letters, perm))
        
        # Replace letters in the equation with their corresponding digits
        moon = int(''.join(str(letter_to_digit[letter]) for letter in 'MOON'))
        soon = int(''.join(str(letter_to_digit[letter]) for letter in 'SOON'))
        june = int(''.join(str(letter_to_digit[letter]) for letter in 'JUNE'))
        
        # Check if the equation holds true
        if moon + soon == june:
            # If it holds true, return the solution
            return letter_to_digit

    return "No solution found"

# Call the function and print the solution
solution = solve_cryptarithm()
print(solution)
