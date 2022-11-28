Kontak = {'Arief': '0812345678', 'Wahyu': '0821345678'}
print('Nama  | Nomor Telepon')
for key, value in Kontak.items():
    print(key, '|', value)
print('kontak Arief : ', Kontak['Arief'])
print()
Kontak['Sigit'] = '0856808391'
print('Tampilkan semua nama')
print(Kontak.keys())
print()
print('Tampilkan semua nomor')
print(Kontak.values())
print()
print('Tampilkan daftar nama dan nomor')
print(Kontak.items())
print()
del Kontak['Wahyu']
print('Tampilkan kontak setelah Wahyu dihapus')
print(Kontak.items())