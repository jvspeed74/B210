class PassageManager:
    def __init__(self):
        # passage storage
        self.library = {
            "The Raven": "Open here I flung the shutter, when, with many a flirt and flutter, In there stepped a stately "
                         "Raven of the saintly days of yore; Not the least obeisance made he; not a minute stopped or stayed "
                         "he; But, with mien of lord or lady, perched above my chamber door— Perched upon a bust of Pallas "
                         "just above my chamber door— Perched, and sat, and nothing more.",
            "Fire and Ice": "Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold "
                            "with those who favor fire. But if it had to perish twice, I think I know enough of hate To say "
                            "that for destruction ice Is also great And would suffice.",
            "Awaking in New York": "Curtains forcing their will against the wind, children sleep, exchanging dreams with "
                                   "seraphim. The city drags itself awake on subway straps; and I, an alarm, awake as a rumor "
                                   "of war, lie stretching into dawn, unasked and unheeded.",
            "I'm thankful that my life doth not deceive": "I’m thankful that my life doth not deceive Itself with a low "
                                                          "loftiness, half height, And think it soars when still it dip its "
                                                          "way Beneath the clouds on noiseless pinion Like the crow or owl, "
                                                          "but it doth know The full extent of all its trivialness, "
                                                          "Compared with the splendid heights above. See how it waits to "
                                                          "watch the mail come in While ’hind its back the sun goes out "
                                                          "perchance. And yet their lumbering cart brings me no word, "
                                                          "Not one scrawled leaf such as my neighbors get To cheer them with "
                                                          "the slight events forsooth, Faint ups and downs of their far "
                                                          "distant friends— And now ’tis passed. What next? See the long "
                                                          "train Of teams wreathed in dust, their atmosphere; Shall I attend "
                                                          "until the last is passed? Else why these ears that hear the "
                                                          "leader’s bells Or eyes that link me in procession? But hark! the "
                                                          "drowsy day has done its task, Far in yon hazy field where stands a "
                                                          "barn, Unanxious hens improve the sultry hour And with contented "
                                                          "voice now brag their deed— A new laid egg—Now let the day decline— "
                                                          "They’ll lay another by tomorrow’s sun.",
        }

    def display_library(self) -> None:
        """
        Prints out the title of each passage in a list format.
        """
        print("Library:")
        for k in self.library.keys():
            print("- ", k)

        print_header()

    def add_new_passage(self):
        """
        A title and text of a new passage is extracted from user and added as an entry in the library.
        """
        print_header("New Passage")
        while True:
            input_title = input("Enter a Title: ")

            if not input_title or input_title.capitalize() == 'Add':
                print("This title cannot exist within the library")
                continue

            if self.is_existing(input_title):
                print("This passage already exists in the library.")
                continue

            break

        while True:
            input_text = input("Enter the passage text (must be over 200 characters): ")

            if len(input_text) < 200:
                print(f"Text length must be at least 200: [Missing {200 - len(input_text)} characters]")
                continue

            break

        self.library[input_title] = input_text

    def is_existing(self, title: str) -> bool:
        """
        Checks if the given title already exists in the library
        """
        # iterate over keys
        for k in self.library.keys():
            if title.lower() == k.lower():  # remove case sensitivity and compare
                return True

        return False


class TextScraper(PassageManager):
    def __init__(self):
        super().__init__()
        self.active_text: str = ""
        self.active_char: str = ""
        self.char_count: int = 0

    def set_active_text(self) -> None:
        """
        Sets the active text to a passage name with the ability to add a passage to the library.
        """
        while True:
            print_header("Select Text")
            # get options
            self.display_library()

            # get input
            user_input = input("Enter a passage name or 'Add' to add your own: ")

            if user_input.capitalize() == "Add":
                self.add_new_passage()
                continue

            # check if in dict and try again if not
            if not self.library.get(user_input, False):
                print(f"Unable to find {user_input} in library.")
                continue

            # key exists in library
            break

        # set value
        self.active_text = user_input
        print_header(self.get_active_text())

    def set_active_char(self) -> None:
        """
        Sets the active character to the extracted value of user input.
        """
        # get input
        while True:
            user_input = input("Enter a character to look for: ")

            # check if it's a single character
            if len(user_input) != 1:
                print("Please enter a single character.")
                continue

            # input valid
            break

        # set value
        self.active_char = user_input

    def search(self) -> None:
        """
        Call the active text from the library and counts the amount of times the active character appears. The value is
        stored in the char_count attribute.
        """
        self.char_count = self.library[self.active_text].count(self.active_char)

    def print_result(self) -> None:
        print_header("Result")
        print(f"'{self.get_active_char()}' occurs {self.get_char_count()} time(s) in {self.get_active_text()}")

    def get_char_count(self) -> int:
        return self.char_count

    def get_active_text(self) -> str:
        return self.active_text

    def get_active_char(self) -> str:
        return self.active_char


def print_header(header=None) -> None:
    """
    Prints a header to the console with a given text inside
    :param header: Optional string to use for the text inside the header.
    """
    if header is None:
        print("=" * 50)

    else:  # calculate the correct amount of "=" and dead space to properly fit header in the center
        width = 50  # total size
        padding = (width - len(header)) // 2  # the amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def main():
    """
    Main Program:
    1. Creates a TextScraper object, which is a subclass of PassageManager, that allows you to search for
    character occurrence in a passage.
    2. Prompts user to select a passage name and a single character to observe.
    3. If the specified character is unable to be found, the program will prompt the user to enter another character.
    Otherwise, the program will display the amount of times the character occurs and end.
    """
    # welcome statement
    print_header("Cipher")
    print("Welcome! This program allows the user to enter a    \n"
          "passage name and a single character. The number of  \n"
          "times the character appears is calculated and       \n"
          "displayed! A new feature is the ability to add your \n"
          "own passage to the library. See below :D")

    # initialize library handler and text scraper
    text_scraper = TextScraper()

    # prompt user for passage name
    text_scraper.set_active_text()

    # infinite loop: repeats until a character is found in text
    while True:
        # get char from user and search text
        text_scraper.set_active_char()
        text_scraper.search()

        # check if character doesn't occur
        if not text_scraper.get_char_count():
            print("Character not found in text. Try another!")
            continue

        # all requirements met
        text_scraper.print_result()
        break


main()
