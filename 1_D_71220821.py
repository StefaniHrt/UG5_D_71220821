def ganti_kata(kalimat, cari, ganti):
    for i in kalimat:
        baru=''
        if i==cari:
            i=ganti  
        baru+=i
        print(baru, end=' ')
    return baru
kalimat=input('Masukkan kalimat:').split()
cari=input('Kata yang dicari:')
ganti=input('Diganti menjadi:')
ganti_kata(kalimat, cari, ganti)