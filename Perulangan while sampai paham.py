"""
Perulangan while membaca buku sampai paham
"""

book_count = 10
print("Read all books until you understand them")

read_count = 0

understood_count = 0
print(f'Number of books read and understood {understood_count}')

while read_count < book_count * 2 - 9:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'The {understood_count + 1} book is not understood yet')
    else:
        understood_count = understood_count + 1
        print(f"The {understood_count} has been read and understood")

print(f"The total number of books that has been read an understood is"
      f" {understood_count} book")
if understood_count == book_count:
    print("bu, semua buku sudah saya baca dan pahami")
else:
    print(f"Not all books are understood by Budi, "
          f"Budi only understand {understood_count} books")