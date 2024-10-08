print("-------------------------------------------------")
print("Nama    : Yardan Raditya Rafi' Widyadhana        ")
print("NIM     : 2409116037                             ")
print("Kelas   : Sistem Informasi A 2024                ")
print("Program : UTS Dasar Pemograman Semester 1        ")
print("-------------------------------------------------")

# Input harga dan kode voucher dari pengguna
harga = float(input("Masukkan nominal harga: "))
kode_voucher = input("Masukkan kode voucher: ")

# Inisialisasi variabel diskon dan batas diskon
diskon = 0
batas_diskon = 0

# Menghitung diskon berdasarkan harga dan kode voucher
if harga > 500_000:
    if kode_voucher == "diskon20":
        diskon = 0.20 * harga
        batas_diskon = 75_000
    else:
        print("\nKode voucher salah.")
elif harga > 300_000:
    if kode_voucher == "diskon15":
        diskon = 0.15 * harga
        batas_diskon = 50_000
    else:
        print("\nKode voucher salah.")
elif harga > 150_000:
    if kode_voucher == "diskon10":
        diskon = 0.10 * harga
        batas_diskon = 20_000
    else:
        print("\nKode voucher salah.")
else:
    print("\nTidak ada diskon untuk harga di bawah 150.000")

# Memastikan diskon tidak melebihi batas maksimal
diskon_terakhir = min(diskon, batas_diskon)

# Menghitung harga akhir setelah diskon
harga_akhir = harga - diskon_terakhir

# Tampilkan harga akhir
print("-------------------------------------------------")
print(f"Harga akhir setelah diskon: Rp {harga_akhir:.2f}")
print("-------------------------------------------------")

# Program selesai