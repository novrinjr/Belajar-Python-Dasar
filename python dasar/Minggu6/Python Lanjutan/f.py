list = [
    'Jarak', 'Suhu', 'Sudut', 'Kecepatan', 'Percepatan', 
    'Hujan', 'Api', 'Kelembapan'
]
sensorDicari = input('Masukkan nama sensor yang dicari: ')
i = 0
while i < len(list):
    if list[i].lower()== sensorDicari.lower():
        print('Sensor pada index: ', i)
        break
    print('Bukan ', list[i])
    i += 1
else:
    print('Maaf sensor yang anda cari tidak ditemukan.')