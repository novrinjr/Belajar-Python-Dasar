a = int(input('Masukkan bil. ganjil lebih dari 50: '))
while a % 2 != 1 or a<=50:
    a=int(input('Salah, masukkan kembali: '))
print('Benar')