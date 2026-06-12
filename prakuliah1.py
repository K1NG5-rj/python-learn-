while True:
    print("Selamat datang di projek sebelum kuliah - RJ")
    print("list projek :")
    print("1. Kalkulator sederhana")
    print("2. nilai siswa")
    print("3. tebak angka")
    choice = input("Pilih projek yang yang ingin di jalankan: ")

    if choice == "kalkulator" or choice == "1" or choice == "kalkulator sederhana":
        while True:
            def kalkulator_sederhana():
             print("Selamat datang di kalkulator sederhana")
            try:
                angka1 = float(input("Masukan angka pertama: "))
                angka2 = float(input("Masukan angka kedua: "))
                operator = input("Masukan operator (+, -, *, /): ")
                if operator == "+" or operator == "tambah":
                    print(f"Hasil penjumlahan dari {angka1} + {angka2} adalah: {angka1 + angka2}")
                elif operator == "-" or operator == "kurang":
                    print(f"Hasil pengurangan dari {angka1} - {angka2} adalah: {angka1 - angka2}")
                elif operator == "*" or operator == "kali":
                    print(f"Hasil perkalian dari {angka1} * {angka2} adalah: {angka1 * angka2}")
                elif operator == "/" or operator == "bagi":
                    print(f"Hasil pembagian dari {angka1} / {angka2} adalah: {angka1 / angka2}")
                else:
                    print("Operator tidak valid. Harap masukkan operator yang benar.")
            except ZeroDivisionError:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
            lanjut = str(input("apakah anda ingin melanjutkan? (y/n): "))
            if lanjut.lower() != "y":
                print("Terima kasih telah menggunakan kalkulator sederhana. Sampai jumpa!")
                break  
        kalkulator_sederhana()

    elif choice == "nilai siswa" or choice == "2":
        while True:
            def nilai_siswa():
             print("Selamat datang di penilaian siswa")
            try:
                nilai = float(input("Masukan nilai akhir anda: "))
                if nilai >= 90:
                    print("Nilai anda A")
                elif nilai >= 80:
                    print("Nilai anda B")
                elif nilai >= 70:
                    print("Nilai anda C")
                elif nilai >= 60:
                    print("Nilai anda D")
                else:
                    print("Nilai anda E")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
            lanjut = str(input("apakah anda ingin melanjutkan? (y/n): "))
            if lanjut.lower() != "y":
                print("Terima kasih telah menggunakan penilaian siswa. Sampai jumpa!")
                break
        nilai_siswa()

    elif choice == "tebak angka" or choice == "3":
        def tebak_angka():
                print("Selamat datang di permainan tebak angka")
                print("Pilih level kesulitan: easy, medium, hard")
                level = input("Masukkan tingkat kesulitan: ")
                import random
                if level == "easy":
                    def easy():
                        while True:
                            tebakan_random = random.randint(0,50)
                            percobaan = 0
                            tebakan = None
                            print("MODE EASY")
                            while tebakan != tebakan_random:
                                try:
                                    tebakan = int(input("Masukkan tebakan anda:"))
                                    percobaan += 1
                                    if tebakan > tebakan_random:
                                        print("kegedean")
                                    elif tebakan < tebakan_random:
                                        print("kekecilan")
                                    else:
                                        print(f"Selamat anda berhasil menebak angka {tebakan_random} dalam {percobaan} percobaan")
                                except ValueError:
                                    print("Input tidak valid. Harap masukkan angka.")
                            lanjut = str(input("apakah anda ingin melanjutkan? (y/n): "))
                            if lanjut.lower() != "y":
                                print("Terima kasih telah bermain tebak angka. Sampai jumpa!")
                            break
                    easy()
                elif level == "medium":
                    def medium():
                        while True:
                            tebakan_random = random.randint(0, 100)
                            percobaan = 0
                            tebakan = None
                            print("MODE MEDIUM")
                            while tebakan != tebakan_random:
                                try:
                                    tebakan = int(input("Masukkan tebakan anda: "))
                                    percobaan += 1
                                    if tebakan > tebakan_random:
                                        print("kegedean")
                                    elif tebakan < tebakan_random:
                                        print("kekecilan")
                                    else:
                                        print(f"Selamat anda berhasil menebak angka {tebakan_random} dalam {percobaan} percobaan")
                                except ValueError:
                                    print("Input tidak valid. Harap masukkan angka.")

                            lanjut = str(input("apakah anda ingin melanjutkan? (y/n): "))
                            if lanjut.lower() != "y":
                                print("Terima kasih telah bermain tebak angka. Sampai jumpa!")
                            break
                    medium()
                if level == "hard":
                    def hard():
                        while True:
                            tebakan_random = random.randint(0,200)
                            percobaan = 0
                            tebakan = None
                            print("MODE HARD")
                            while tebakan != tebakan_random:
                                try:
                                    tebakan = int(input("Masukkan tebakan anda: "))
                                    percobaan += 1
                                    if tebakan > tebakan_random:
                                        print("kegedean")
                                    elif tebakan < tebakan_random:
                                        print("kekecilan")
                                    else:
                                        print(f"Selamat anda berhasil menebak angka {tebakan_random} dalam {percobaan} percobaan")
                                except ValueError:
                                    print("Input tidak valid. Harap masukkan angka.")
                            lanjut = str(input("apakah anda ingin melanjutkan? (y/n): "))
                            if lanjut.lower() != "y":
                                print("Terima kasih telah bermain tebak angka. Sampai jumpa!")
                            break
                    hard()
                else:
                    print("Tingkat kesulitan tidak valid. Harap masukkan tingkat kesulitan yang benar.")
        tebak_angka()
    else:
        print("Pilihan tidak valid. Harap masukkan pilihan yang benar.")

    end = str(input("kembali ke menu? (y/n): "))
    if end.lower() == "n":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break