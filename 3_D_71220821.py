import math
while True:
    jarak=input('Masukkan jarak awal (dalam meter):')
    sudut1=int(input('Masukkan sudut elevasi pada menit ke-5 (dalam derajat):'))
    sudut2=int(input('Masukkan sudut elevasi pada menit ke-6 (dalam derajat):'))
    if jarak!='stop' or jarak!='berhenti':
        j=int(jarak)
        tinggi=j*math.tan(sudut1)
        jakhir=j*math.tan(sudut2)-math.tan(sudut1)
        selisih=jakhir*math.tan(sudut2)
    elif jarak=='stop' or jarak=='berhenti':
        break
    print(tinggi)
    print(jakhir)
    print(selisih)