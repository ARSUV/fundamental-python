# List sebagai iterable
print('\n')
gorengan = 'bakwan', 'cireng', 'tahuisi', 'tempegoreng', 'ubigoreng'

for g in gorengan:
    for karakter in g:
        print(karakter)
    print(g)
    print('total', len(g), 'karakter')
print('\ntotal', len(gorengan), 'macam gorengan')

# String sebagai iterable
print('\n')
gorengan = 'bakwan'
for i in gorengan:
    print(i)
print('total', len(gorengan), 'karakter')

# For didalam for
print('\n')
buah = 'semangka', 'jeruk', 'apel', 'anggur'
sayur = 'kangkung', 'wortel', 'tomat', 'kentang', 'cabai'
daftarbelanja = (buah + sayur)
# print(daftarbelanja)
for subdaftarbelanja in daftarbelanja:
    print(subdaftarbelanja)
print('total jumlah belanja ada', len(daftarbelanja), 'macam')
