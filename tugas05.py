# Soal No 1
print("====No 01======")
kendaraan = ['ThunderBlade 250', 'Sepeda motor sport', '250cc', 'Hitam doff dengan aksen merah', '2']
print(kendaraan)

# Menambahkan data tambahan
kendaraan.append("Sportbike")
kendaraan.append('60 juta')
print(kendaraan)

# Menambahkan Yamaha R25 setelah elemen 'Sepeda motor sport'
index_of_type = kendaraan.index('Sepeda motor sport')
kendaraan.insert(index_of_type + 1, 'Yamaha R25')
print(kendaraan)
print("===============")

# Soal No 2
print("=====No 2 ============")

pilih = int(input(("""
Selamat datang di aplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga
Masukkan pilihan anda: """)))

match pilih:
    case 1:
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukkan nilai sisi: "))
        hitung = sisi * sisi
        print("Luas persegi yang sisinya", sisi, "adalah", hitung)
    case 2:
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        r = int(input("Masukkan jari-jari: "))
        luas = 3.14 * r * r
        print("Luas lingkaran dengan jari-jari", r, "adalah", luas)
    case 3:
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas)
    case _:
        print("Pilihan angka tidak dikenali")
