class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        for username,books in self.rented_books.items():
            for book,days in books.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days} days!'
        # continue with happy case
        for avail_book in self.books_available[author]:
            if avail_book == book_name:
                self.books_available[author].remove(avail_book)

                if user.username in self.rented_books:
                    self.rented_books[user.username][book_name] = days_to_return
                else:
                    self.rented_books[user.username] = {book_name:days_to_return}
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"


    def return_book(self, author, book_name, user):
        if not book_name in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        #happy case
        user.books.remove(book_name)
        self.rented_books[user.username].pop(book_name)
        self.books_available[author].append(book_name)


"""
dic = {author:[bookname1,bookname2]}
dic_rented = {username:{bookname:days,booknane2:days2}}
"""