# 1. Input nilai tugas, UTS, UAS, dan kehadiran mahasiswa
nilai_tugas = float(input("Nilai tugas : "))
nilai_uts = float(input("Nilai UTS   : "))
nilai_uas = float(input("Nilai UAS   : "))
kehadiran = float(input("Kehadiran   : "))

# 2. Hitung nilai akhir dengan rumus yang ditentukan
nilai_akhir = (0.20 * nilai_tugas) + (0.30 * nilai_uts) + (0.50 * nilai_uas)

# 3, 4, 5, 6. Logika penentuan status kelulusan dan predikat
if nilai_akhir >= 75 and kehadiran >= 80:
    # Cek apakah memenuhi syarat LULUS DENGAN PREDIKAT
    if nilai_akhir >= 85 and kehadiran >= 90 and (nilai_akhir % 2 == 0):
        status = "LULUS DENGAN PREDIKAT"
    else:
        status = "LULUS"
else:
    status = "BELUM LULUS"

# Menampilkan hasil output
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Status      : {status}")
