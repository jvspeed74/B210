"""
Name: Jalen Vaughn
Date: 3/21/24
File: main.py
Description: This script contains the solution to question 2
Dependencies/Imports: None
"""


class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_header(header=None) -> None:
        """
        Prints a header to the console with a given text inside
        :param header: Optional string to use for the text inside the header.
        """
        
        if header is None:
            print("=" * 50)
            return
        
        # Calculate the correct amount of "=" and dead space to properly fit header in the center
        width: int = 50  # Total size
        padding: int = (width - len(header)) // 2  # The amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def decode_acrostic(acrostic: str, first_line: int = 0, char_start_pos: int = 0, delimiter: str = "\n") -> None:
    """
    Decodes an acrostic poem and prints the result.
    :param acrostic: The acrostic poem string.
    :param first_line: The starting position for iterating through lines (optional).
    :param char_start_pos: The starting position for iterating through characters in each line (optional).
    :param delimiter: The character that separates lines in the acrostic poem (optional).
    """
    
    # Split acrostic string by its delimiter.
    acrostic_list: list[str] = acrostic.split(sep=delimiter)
    
    # Iterate over each line and append the first alphabetic character to the output.
    secret_message: str = ""
    for line in acrostic_list[first_line:]:
        for char in line[char_start_pos:]:
            # Ensure we grab the first alphabetic character.
            if char.isalpha():
                secret_message += char
                break
    
    # Display the result to the user.
    print(secret_message)


def main():
    """
    Main entry point of the program. Each test case within the program will run through the decode_acrostic function and
    display the result.
    """
    
    # Declare test cases
    test_a_cases = [
        ("SATOR\nAREPO\nTENET\nOPERA\nROTAS\n", 0),
    ]
    
    test_b_cases = [
        ('Elizabeth it is in vain you say\t'
         '“Love not” – thou sayest it in so sweet a way:\t'
         'In vain those words from thee or L.E.L.\t'
         'Zantippe’s talents had enforced so well:\t'
         'Ah! If that language from thy heart arise,\t'
         'Breath it less gently forth — and veil thine eyes.\t'
         'Endymion, recollect, when Luna tried\t'
         'To cure his love – was cured of all beside\t'
         'His folly – pride – and passion – for he died.', 0, 0, "\t")
    ]
    
    # Run Test A parameters through the decode_acrostic function
    for test in test_a_cases:
        for i in range(5):
            Utils.print_header(f"Test A: {i + 1}")
            decode_acrostic(*test, char_start_pos=i)
    
    else:
        Utils.print_header("Test A Complete")
        print("\n")
    
    # Run Test B parameters through the decode_acrostic function
    for count, test in enumerate(test_b_cases):
        Utils.print_header(f"Test B: {count + 1}")
        decode_acrostic(*test)
    else:
        Utils.print_header("All Tests Complete")


main()
