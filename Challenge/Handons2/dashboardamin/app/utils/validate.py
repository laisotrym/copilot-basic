# constants
USERNAME_MIN_LENGTH = 5
USERNAME_MAX_LENGTH = 50


class Utils:

    @staticmethod
    def is_valid_email(email):
        import re
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email)

    @staticmethod
    # no need to test this method
    def is_valid_username(username):
        return USERNAME_MIN_LENGTH < len(username) < USERNAME_MAX_LENGTH
