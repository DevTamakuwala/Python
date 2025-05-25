class Book:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def Display(self):
        print(f"Book Title :-: {self.title}")
        print(f"Book Author:-: {self.author}")
        print(f"Book Price:-:{self.price}")

dispaly1 = Book("C++","XYZ",1600)
dispaly2 = Book("Java","abc",1800)

print(dispaly1.Display())
print()
print(dispaly2.Display())

