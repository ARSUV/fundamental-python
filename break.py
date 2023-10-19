number = 5  # jika angka di ganti melebihi range 40 maka menghasilkan else print (angka tidak ditemukan)
for i in range(0, 40):
    print(i)
    if i is number:
        print('angka', number, 'di temukan')
        break
else:
    print('angka tidak ditemukan')
