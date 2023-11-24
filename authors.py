class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
class Library:
    def __init__(self):
        self.books = []
        self.books.append(Book("A Tale of Two Cities", "Charles Dickens", 191.99))
        self.books.append(Book("The Lord of the Rings", " J.R.R. Tolkien", 1666.99))
        self.books.append(Book("The Little Prince", "Antoine de Saint-Exupéry", 91.99))
        self.books.append(Book("The Hobbit", " J.R.R. Tolkien", 1406.99))
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")
    def update_book(self, title, new_title=None, new_author=None, new_price=None):
        for book in self.books:
            if book.title == title:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_price:
                    book.price = new_price
                print(f"Book '{title}' updated successfully.")
                return
        print(f"Book '{title}' not found.")
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print(f"Book '{title}' not found.")
    def search_books(self, key, value):
        results = []
        for book in self.books:
            if key == 'title' and value.lower() in book.title.lower():
                results.append(book)
            elif key == 'author' and value.lower() in book.author.lower():
                results.append(book)
            elif key == 'price' and str(value) in str(book.price):
                results.append(book)
        if results:
            print(f"Search results for {key} '{value}':")
            for result in results:
                print(f"Title: {result.title}, Author: {result.author}, Price: {result.price}")
        else:
            print(f"No books found for {key} '{value}'.")
def main():
    library = Library()
    while True:
        print("\nOptions:")
        print("1. Search for a book")
        print("2. Add a book")
        print("3. Update book")
        print("4. Remove a book")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            key = input("Enter search criteria (title/author/price): ")
            value = input("Enter search value: ")
            library.search_books(key, value)
        elif choice == '2':
            title = input("Enter title: ")
            author = input("Enter author: ")
            try:
                price = float(input("Enter price: "))
            except ValueError:
                print("Invalid price format. Please enter a valid number.")
                price = float(input("Enter price: "))

            new_book = Book(title, author, price)
            library.add_book(new_book)
        elif choice == '3':
            title = input("Enter title of the book to update: ")
            new_title = input("Enter new title (press Enter to keep current title): ")
            new_author = input("Enter new author (press Enter to keep current author): ")
            new_price = input("Enter new price (press Enter to keep current price): ")
            try:
                new_price = float(new_price)
            except ValueError:
                print("Invalid price format. Please enter a valid number.")
                new_price = input("Enter new price (press Enter to keep current price): ")

            new_price = input("Enter new price (press Enter to keep current price): ")
            library.update_book(title, new_title, new_author, new_price)
        elif choice == '4':
            title = input("Enter title of the book to remove: ")
            library.remove_book(title)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    main()