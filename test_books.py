books_list = []
with open('C:/Users/TAvram/Desktop/100daysPython/some_books.txt') as f:
    books_list = f.readlines()

print (books_list)


books_list2 = []
for i in books_list:
    j = i.replace("\n", "")
    books_list2.append(j)

print(books_list2)

books_code = []
for i in books_list2:
    books_code.append(i[0] + str(len(i)))

print(books_code)