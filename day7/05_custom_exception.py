# This code defines a custom exception called InvalidAgeError, which is raised when a user attempts to vote with an age less than 18. The vote function checks the age and raises the exception if the user is not eligible. The main function prompts the user for their age and handles the InvalidAgeError by printing an error message.
class InvalidAgeError(Exception):
    pass


def vote(age):
    if age < 18:
        raise InvalidAgeError("Not eligible for voting.")
    print("You are eligible to vote.")


def main():
    try:
        age = int(input("Enter your age: "))
        vote(age)
    except ValueError:
        print("Please enter a valid integer for age.")
    except InvalidAgeError as e:
        print(e)


main()
# Output: Input: 16
# Output: Not eligible for voting.
# Input: 20
# Output: You are eligible to vote.
