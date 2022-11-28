Kontak = {'Ari': '081267888', 'Dina': '087677776'}
print('Nama  | Nomor Telepon')
for key, value in Kontak.items():
    print('=======================')
    print('#',key, '|', value)
print()
print('Tampilkan kontaknya Ari')
print('kontak Ari : ', Kontak['Ari'])
print()
print('Tambah kontak baru dengan nama Riko')
Kontak['Riko'] = '087654544'
print(Kontak)
print()
print('Ubah kontak Dina dengan nomor barunya')
Kontak['Dina'] = '088999776'
print()
print('Tampilkan semua nama')
print(Kontak.keys())
print()
print('Tampilkan semua nomor')
print(Kontak.values())
print()
print('Tampilkan daftar nama dan nomor')
print(Kontak.items())
print()
print('Hapus kontak Dina')
del Kontak['Dina']
print(Kontak)