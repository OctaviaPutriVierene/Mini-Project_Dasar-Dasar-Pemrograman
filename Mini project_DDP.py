nama_hewan =[]
jenis_hewan =[]
status_makan =[]
status_minum =[]
while True:
    print("Sistem monitoring hewan peliharaan harian")
    print("1. Tampilkan semua hewan peliharaan")
    print("2. Cari hewan peliharaan")
    print("3. Update status makan")
    print("4. Update status minum")
    print("5. Tambah hewan peliharaan")
    print("6. Hapus data hewan peliharaan (mati/lepas)")
    print("7. Reset semua status (Hari baru)")
    print("8. Keluar")
    pilihan = input("Menu (1-8)")

    if pilihan == "1":
        print("\n Daftar hewan peliharaan saat ini")
        if len(nama_hewan) == 0:
            print("Tidak ada nama hewan pada daftar")
        else:
            for i in range(len(nama_hewan)):
                print(f"{i+1}. {nama_hewan[i]}  ({jenis_hewan[i]})")
                print(f"[Makan: {status_makan[i]}]")
                print(f"[Minum: {status_minum[i]}]")

    elif pilihan == "2":
        print("Cari hewan peliharaan")
        if len(nama_hewan) == 0:
            print("Daftar hewan tidak ada")
        else:
            cari = input("Masukkan nama hewan yang dicari: ")
            ketemu = False
            for i in range(len(nama_hewan)):
                if cari.lower() in nama_hewan[i].lower():
                    print(f"\n[Ditemukan] Nomor: {i+1}")
                    print(f"Nama: {nama_hewan[i]}  ({jenis_hewan[i]})")
                    print(f"Makan: {status_makan[i]}")
                    print(f"Minum: {status_minum[i]}")
                    ketemu = True
            if not ketemu:
                print(f"Hewan dengan nama '{cari}' tidak ditemukan")

    elif pilihan == "3":
        print("\n Update status makan")
        if len(nama_hewan) == 0:
            print("Belum ada hewan dalam daftar")
        else:
            for i in range(len(nama_hewan)):
                print(f"{i+1}. {nama_hewan[i]} Makan: {status_makan[i]}")
            nomor = int(input("Pilih nomor hewan yang sudah diberi makan:"))
            index = nomor - 1
            if 0 <= index <len(nama_hewan):
                status_makan[index] = "Sudah"
                print(f"Berhasil status sudah di update")
            else:
                print("Nomor tidak ada")

    elif pilihan == "4":
        print("\n Update status minum")
        if len(nama_hewan) == 0:
            print("Belum ada hewan dalam daftar")
        else:
            for i in range(len(nama_hewan)):
                print(f"{i+1} {nama_hewan[i]} Minum: {status_minum[i]}")
            nomor = int(input("Pilih nomor hewan yang sudah diberi minum: "))
            index = nomor -1
            if 0 <= index < len(nama_hewan):
                status_minum[index] = "Sudah"
                print(f"Berhasiil status sudah di update")
            else:
                print("Nomor tidak ada")

    elif pilihan == "5":
        print("\n Tambah hewan peliharaan baru")
        nama= input("Masukkan nama hewan:")
        jenis = input("Masukkan jenis Kucing/Anjing:")
        nama_hewan.append(nama)
        jenis_hewan.append(jenis)
        status_makan.append("Belum")
        status_minum.append("Belum")
        print(f"Yeyyyyyyyyyyyy {nama} berhasil ditambahkan><")

    elif pilihan == "6":
        print("\n Hapus data peliharaan")
        if len(nama_hewan) == 0:
            print("Tidak ada data hewan yang bisa di hapus")
        else:
            for i in range(len(nama_hewan)):
                print(f"{i+1}. {nama_hewan[i]} ({jenis_hewan[i]})")
            nomor = int(input(" Pilih nomor hewan yang akan di hapus dari daftar: "))
            index= nomor - 1
            if 0 <= index < len(nama_hewan):
                nama_dihapus = nama_hewan.pop(index)
                jenis_hewan.pop(index)
                status_makan.pop(index)
                status_minum.pop(index)
                print(f" Data {nama_dihapus} telah dihapus")
            else:
                print("Nomor tidak ada")

    elif pilihan == "7":
        print("\n Reset harian")
        if len(nama_hewan) == 0:
            print("Belum ada hewam dalam daftar")
        else:
            yakin = input("Apakah kamu ingin mereset semua status?(ya/tidak)")
            if yakin.lower() == "ya":
                for i in range (len(status_makan)):
                    status_makan[i] = "Belum"
                    status_minum[i] = "Belum"
                print("Semua status hewan telah di reset")

    elif pilihan == "8":
        print("\n Terimakasih")
        break
    else:
        print("\n Pilihan salah masukkan angka 1-8")