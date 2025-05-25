class Library:
    def __init__(self):
        self.acc_number = None
        self.title = None
        self.author = None
        self.publisher = None

    def read(self):
        self.acc_number = input("Enter Accession Number: ")
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Author Name: ")
        self.publisher = input("Enter Publisher Name: ")

    def compute_fine(self):
        days_late = int(input("Enter the number of days late: "))
        fine = days_late * 5
        print(f"Fine for {days_late} days late: Rs. {fine}")

    def display(self):
        print("\nBook Details:")
        print(f"Accession Number: {self.acc_number}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")

# Main execution
library_book = Library()
library_book.read()
library_book.compute_fine()
library_book.display()
