"""
You give a name of a person and the system guesses the bio of the person
"""
from faker import Faker
class GuessBio:
    """
    The class guess the bio of a person given
    first name and last name
    """
    def __init__(self, first_name, last_name):
        """
        constructor class
        :param first_name: str
        :param last_name: str
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def is_string(string):
        """
        Check if text is actually a string
        :return: None if okay and raise error if not
        """
        if not isinstance(string, str):
            raise TypeError(f"{string} must be a string")

    def guess_bio(self):
        """
        Guess the bio of a person
        :return: str
        """
        self.is_string(self.first_name)
        self.is_string(self.last_name)
        address = Faker().address()
        phone = Faker().phone_number()
        email = Faker().email()
        return {
            "First name": self.first_name,
            "Last name": self.last_name,
            "address": address,
            "phone": phone,
            "email": email
        }

if __name__ == "__main__":
    obj = GuessBio("John", "Mwangi")
    print(obj.guess_bio())




