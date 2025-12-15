books = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
}

def search_books():
    print("Search for books:")
    while True:
        author = input("Enter the author's name: ")
        
        if author in books:
            book_name = list(books.keys())[list(books.values()).index(author)]
            
            print(f"Book '{book_name}' by {author} found!")
        else:
            print(f"No book found with the name '{author}'.")
        
        again = input("Do you want to search another book? (yes/no): ")
        if again.lower() != "yes":
            break

def search_authors():
    print("Search for authors:")
    while True:
        author = input("Enter the author's name: ")
        
        if author in books:
            print(f"Author '{author}' found!")
        else:
            print(f"No author found with the name '{author}'.")
        
        again = input("Do you want to search another author? (yes/no): ")
        if again.lower() != "yes":
            break

search_books()
search_authors()