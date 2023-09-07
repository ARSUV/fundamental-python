"""
Perulangan membaca buku while
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua buku"')

jumlah_buku_yang_dibaca = 0
print(f'jumlah buku yang di baca {jumlah_buku_yang_dibaca}')

while jumlah_buku_yang_dibaca < jumlah_buku:
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f"buku ke {jumlah_buku_yang_dibaca}  sudah di baca")

print(f'Total buku yang sudah di baca adalah {jumlah_buku_yang_dibaca} buku')
