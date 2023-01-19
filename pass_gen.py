"""
Generate a random password of specified length and writes it into a markdown file containing new and previous passwords.
"""
import string
import random


def str_to_bool(answer: str) -> bool:
    """
    Convert a string into a boolean.
    :param answer: "Yes" or "No" string.
    :return: Boolean representation of the string.
    :raises ValueError: if not y or n.
    """
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:  # Produce an error if user gives answer besides y or n
        raise ValueError(f"{answer} not a valid answer.")


def generate_password(length: int, special_chars: bool) -> str:
    """
    Generates a random password of specific length using uppercase letters, lowercase letters, and digits.
    :param length: The desired length of the generated password.
    :param special_chars: Whether to include special characters in the generated password.
    :return: Randomly generated password.
    """
    # Only include special characters if the user wishes to include them
    if special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    # Add random character until desired length is reached
    password = "".join(random.choice(characters) for i in range(length))
    return password


def write_to_markdown(file_name: str, string_to_write: str) -> None:
    """
    Write a string into a Markdown file. If the file already contains content,then add a newline before writing the new
    content.
    :param file_name: Name of the Markdown file to write to.
    :param string_to_write: String value to write to the Markdown file.
    :return: None.
    """
    with open(file_name, 'a') as f:
        f.write("\n" + string_to_write)  # Always add a new line before writing new string


def initialize_file(file_name: str) -> None:
    """
    Initialize a Markdown file.
    :param file_name: Name of the Markdown file.
    :return: None.
    """
    with open(file_name, 'r') as file:
        current_content = file.read()
        if current_content:  # Do not write headings if the file has already been initialized
            pass
        else:
            with open(file_name, 'a') as f:
                f.write("Site \t\t Password")


def if_you_write(file_name: str, password: str) -> None:
    """
    Display if user wishes to save password.
    :param file_name: Name of the file to write to.
    :param password: Generated password.
    :return: None.
    """
    site = input("What site is this password for? ")
    print(f"Okay, saving password for {site} to {file_name}!")  # Debugging output
    string_to_print = f"{site} \t\t {password}"
    initialize_file(file_name)
    write_to_markdown(file_name, string_to_print)
    print(f"Password successfully saved to {file_name}!")


def main():
    length = int(input("Number of characters: "))
    special_chars = input("Would you like to include special characters? (y/n): ")
    answer = str_to_bool(special_chars)
    print("Okay, generating your password!")  # Debugging output
    password = generate_password(length, answer)
    print(f"Here's your password! Make sure you don't share it with anyone!")
    print(f"\t{password}")
    file_name = "output/passwords.md"
    write_md = input(f"Would you like to save this password to {file_name}? (y/n): ")
    if str_to_bool(write_md):
        if_you_write(file_name, password)
    # Add a failsafe just in case the user did want to save their password and made a mistake
    else:
        you_sure = input("Are you sure you don't want to save your password? (y/n): ")
        answer = str_to_bool(you_sure)
        if answer:
            print("Okay, your password won't be saved!")
        else:
            if_you_write(file_name, password)


if __name__ == "__main__":
    main()
