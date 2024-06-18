If the user chooses to add a new library, it prompts for the library ID, creates a new Library object, and adds it to the libraries list.
If the user chooses to add a new book to a library, it asks for the library ID, looks for the corresponding Library object, and if found, asks for the book details, creates a new Book object, and adds it to the library's books list. adds
If the user chooses to remove a book from a library, it asks for the library ID and book name, looks for the corresponding Library and Book object, and if found, removes the book from the library.
If the user chooses to edit a book, it prompts for the library ID and book name, looks for the corresponding Library and Book object, and if found, prompts for new book details and updates the book properties.
If the user chooses to print library information, it asks for the library ID, looks for the corresponding Library object, and if found, prints the library ID and the list of books in the library.
If the user chooses to exit the program, it calls the save_libraries() function to save the updated library and book information to files and exits the loop.
