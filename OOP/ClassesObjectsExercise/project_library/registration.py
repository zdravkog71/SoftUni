class Registration:
    def add_user(self, user, library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user, library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"

        library.user_records.remove(user)

    def change_username(self, user_id, new_username, library):

        for user in library.user_records:
            if user.user_id == user_id:
                old_username = user.username
                if old_username == new_username:
                    return f"Please check again the provided username - it should be different than the username used so far!"
                else:
                    for one_username in library.rented_books:
                        if one_username == old_username:
                            value = library.rented_books.pop(old_username)
                            library.rented_books[new_username] = value

                    user.username = new_username

                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"There is no user with id = {user_id}!"


