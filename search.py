books = {"1984": "George Orwell", "The Shining" : "Stephen King", "Emma" : "Jane Austen"}
while True:
    print("1. Search book\n2. Search author\n3. Exit\n")
    n = input("Enter your choice: ")
    if(n==1):
        book = input("Enter book name: ")
        if(book in books.keys):
            print("Book Found!")
            print(f"{book} by {books[book]}")
        else:
            print("Book not found!")
    if(n==2):
        author = input("Enter author name: ")
        if(author in books.items):
            print("Author Found!")
            print(f"{book} by {books[book]}")
        else:
            print("Author not found!")
    if(n==3):
        break