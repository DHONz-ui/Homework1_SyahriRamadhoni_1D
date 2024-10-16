nama = input('Masukan Nama : ')
umur = int(input('Masukan umur : '))
jenis_kelamin = input('Masukan Jenis Kelamin : ')
tinggi_badan = int(input('Masukan Tinggi Badan : '))
nilai_ijazah = float(input('Masukan Nilai Ijazah : '))
kewarganegaraan = input('Masukan Kewarganegaraan : ')
jenis_kelamin_yang_memenuhi = ['pria','Pria','laki laki','Laki laki']
kewarganegaraan_yang_memenuhi = ['indonesia','Indonesia']
biaya_administrasi = float(input('Masukan Biaya Administrasi : '))
hasil = 'SELAMAT ANDA LOLOS KE TAHAP BERIKUTNYA' if umur < 28 and tinggi_badan >= 170 and nilai_ijazah >= 8.0  and biaya_administrasi == 100.000 and jenis_kelamin in jenis_kelamin_yang_memenuhi and kewarganegaraan in kewarganegaraan_yang_memenuhi else 'MAAF COBA LAGI SEMANGAT TERUS'
print(hasil)