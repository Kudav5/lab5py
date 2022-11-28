print('Program Input Nilai')
print('===================')

data = {
    'NIM': '',
    'Nama': '',
    'Nilai UTS': '',
    'Nilai UAS': '',
    'Nilai Tugas': '',
}
z = data.copy()
while True:
    a = input('[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ')
    if a=='T':
        print('Tambah data')
        b = input('Nama: ')
        data['Nama'] = b
        c = input('NIM: ')
        data['NIM'] = c
        d = input('Nilai UTS: ')
        data['Nilai UTS'] = d
        e = input('Nilai UAS: ')
        data['Nilai UAS'] = e
        f = input('Nilai Tugas: ')
        data['Nilai Tugas'] = f
        g = float(f)*0.3 + float(d)*0.35 + float(e)*0.35
    elif a=='U':
        h = input('Ubah NAMA/NIM/TUGAS/UTS/UAS: ')
        if h=='NAMA':
            b = input('Nama: ')
            data['Nama'] = b
        elif h=='NIM':
            c = input('NIM: ')
            data['NIM'] = c
        elif h=='UTS':
            d = input('Nilai UTS: ')
            data['Nilai UTS'] = d
        elif h=='UAS':
            e = input('Nilai UAS: ')
            data['Nilai UAS'] = e
        elif h=='TUGAS':
            f = input('Nilai Tugas: ')
            data['Nilai Tugas'] = f
    elif a=='H':
        # data.pop('NIM')
        # data.pop('Nama')
        # data.pop('Nilai UTS')
        # data.pop('Nilai UAS')
        # data.pop('Nilai Tugas')
        # data['Nama']
        # data['NIM']
        # data['Nilai UTS']
        # data['Nilai UAS']
        # data['Nilai Tugas']
        print(z)
        
    elif a=='C':
        print()
    elif a=='L':
        print(dict(data))
        print('Daftar Nilai')
        print('============================================================')
        print('|  NO  |  NIM  |  Nama  |  Tugas  |  UTS  |  UAS  |  AKHIR |')
        print('============================================================')
        print('|  1   |  ', data['NIM'], '  |  ', data['Nama'], '  |  ', data['Nilai Tugas'], '  |  ', data['Nilai UTS'], '  |  ', data['Nilai UAS'], '  |  ', g, '  |  ')
    elif a=='K':
        break

