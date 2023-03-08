def hitung_mobil():
    jumlahSol=0
    jumlahSur=0
    jumlahJog=0
    jumlahMag=0
    while True:
        asal=input('Masukkan asal mobil (ketik"done" untuk keluar):').lower()
        if asal=='solo':
            jumlahSol+=1
        elif asal=='surabaya':
            jumlahSur+=1
        elif asal=='jogja':
            jumlahJog+=1
        elif asal=='magelang':
            jumlahMag+=1
        elif asal=='done':
            break 

    print('Jumlah Mobil Solo :',jumlahSol)
    print('Jumlah Mobil Surabaya :',jumlahSur)
    print('Jumlah Mobil Jogja :',jumlahJog)
    print('Jumlah Mobil Magelang :',jumlahMag)
hitung_mobil()