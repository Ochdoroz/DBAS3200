import csv

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = int(year_published)

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Published: {self.year_published}")

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = []

    def load_books(self):
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        title, author, year_published = row
                        self.books.append(Book(title.strip(), author.strip(), year_published.strip()))
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty library.")
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        try:
            with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                for book in self.books:
                    try:
                        writer.writerow([book.title, book.author, book.year_published])
                    except Exception as e:
                        print(f"Error writing book {book.title}: {e}")
            print(f"CSV file '{self.filename}' written successfully.")
        except IOError as e:
            print(f"File error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def filter_books_by_year(self):
        print('Enter the year your looking for')
        try:
            year = int(input())
            filtered_books = [book for book in self.books if book.year_published == year]
            if filtered_books:
                print(f"\nBooks published in the year {year}:")
                for book in filtered_books:
                    book.describe()
            else:
                print(f"\nNo books found for the year {year}.")
                return
        except ValueError:
            print("Invalid year entered. Please enter a valid number.")

    def find_books_by_author(self):
        print('Enter the authors name you are looking for')
        author = input()
        filtered_books = [book for book in self.books if book.author == author]
        if filtered_books:
            print(f"\nBooks published by {author}:")
            for book in filtered_books:
                book.describe()
        else:
            print(f"No books found by {author}.")
            return

    def show_all_books(self):
        print("\nAll Books:")
        for book in self.books:
            book.describe()

    def add_new_book(self):
        print('Add a new book by entering the title:')
        title = input("Title: ")
        author = input("Author: ")
        year_published = input("Year Published: ")
        if not year_published.isdigit():
            print('Year must be a number')
            return

        new_book = Book(title, author, year_published)
        self.books.append(new_book)
        self.save_books()
        print("New book added successfully.")

    def remove_book(self):
        print('Enter the title of the book you want to remove')
        title = input().lower
        for book in self.books:
            if book.title.lower() == title:
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                self.save_books()
                return
        print(f"Book '{title}' not found.")


def main():
    library = Library('books.csv')
    library.load_books()
    print("\nLoaded Books:")
    library.show_all_books()
    while True:
        print("\nWelcome to the Library System")
        print("1. Show all books")
        print("2. Add a new book")
        print("3. Search books by author")
        print("4. Filter books by year")
        print("5. Remove book")
        print("6. Exit")
        choice = input()

        if choice == "1":
            library.show_all_books()
        elif choice == "2":
            library.add_new_book()
        elif choice == "3":
            library.find_books_by_author()
        elif choice == "4":
            library.filter_books_by_year()
        elif choice == "5":
            library.remove_book()
        elif choice == "6":
            print("Exiting the library system. Goodbye!")
            library.save_books()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
