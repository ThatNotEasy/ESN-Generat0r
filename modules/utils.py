import random

class Utils:
    @staticmethod
    def to_int(txt):
        return int(txt)

    @staticmethod
    def random_string(length=64):
        chars = "0123456789ABCDEF"
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def take_char(txt, length):
        """Take a substring of a specified length from the string."""
        if txt is None or txt == "":
            raise ValueError("String is empty")
        
        return txt[:length]
