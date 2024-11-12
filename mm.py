# Basic Python Program

# Function to calculate years to reach 100
def years_to_100(age):
    years_left = 100 - age
    return years_left

# Main program
def main():
    # Asking for user input
    name = input("What is your name? ")
    age = int(input(f"Hello, {name}! How old are you? "))
    
    # Checking if the user is already 100 or more
    if age >= 100:
        print(f"Wow, {name}, you're already {age} years old!")
    else:
        # Calculating and printing years to reach 100
        years_left = years_to_100(age)
        print(f"Hey {name}, you will be 100 years old in {years_left} years.")
    
    # Loop to ask the user if they want to run the program again
    while True:
        run_again = input("Do you want to run the program again? (yes/no): ").lower()
        if run_again == "yes":
            main()  # Restart the program
        elif run_again == "no":
            print("Goodbye! Have a great day!")
            break  # Exit the loop and end the program
        else:
            print("Please answer with 'yes' or 'no'.")

# Run the program
if __name__ == "__main__":
    main()
