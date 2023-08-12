# QUESTION 2
print("\nNESTED DICTIONARY\n\n")

# part a:
books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } } 
print(books)
print("\n\n\n\n")
books['book4']={'title':'power of subconcious mind','author':'joseph murphy','year':1930}
print(books)

# part b
print("\nprint title of books\n")
for i in books:
  print(books[i]['title'])


# part c
min_year = min(books[i]['year'] for i in books)
for i in books:
    if books[i]['year'] == min_year:
        print("\n\nThe book with the earliest publication year is: ", books[i] 
        ['title'], "by", books[i]['author'])
