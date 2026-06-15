nilai_xtkj = {
    "Damas": 90,
    "Dimas": 85,
    "Dumus": 92,
}
print("Selamat datang di program nilai siswa XTKJ")
while True:
    try:
        x = input("tambah, hapus, lihat, cari atau keluar: ")
        if x == "tambah":
            nama = input("Nama: ")
            nilai = int(input("Nilai: "))
            nilai_xtkj[nama.capitalize()] = nilai
        elif x == "hapus":
            nama = input("Nama: ")
            if nama.capitalize() not in nilai_xtkj:
                print("Nama tidak ditemukan")
            else:   
                del nilai_xtkj[nama.capitalize()]
        elif x == "lihat":
            for list in nilai_xtkj:
                print(list, ":", nilai_xtkj[list])
        elif x == "cari":
            cari = input("Nama: ")
            if cari.capitalize() not in nilai_xtkj:
                print("Nama tidak ditemukan")
            else:
                print("siswa dengan nama", cari.capitalize(), "ditemukan dengan nilai", nilai_xtkj[cari.capitalize()])
        elif x == "keluar":
            break
        else:
            print("Perintah tidak dikenali")
    except:
        print("Terjadi kesalahan, pastikan input benar")