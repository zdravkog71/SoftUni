class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_char = [ch for ch in value if ch.isupper()]
        is_digit = [ch for ch in value if ch.isdigit()]
        if not is_length_valid or not is_upper_char or not is_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        result = f"You have a profile with username: "
        result += f'"{self.__username}" and password: {"*" * len(self.__password)}'
        return result






#profile_with_invalid_password = Profile('My_username', 'My-password')
#profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

