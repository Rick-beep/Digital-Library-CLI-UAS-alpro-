'''
Christian Gilbert Rusianto (202565001)

https://github.com/Rick-beep
https://github.com/Rick-beep/Digital-Library-CLI-UAS-alpro-

'''

import json
class Ebook():
    def __init__(self, data_dic):
        self.data = data_dic
        self.load()
    
    def __str__(self):
        return f"kode: {self.kode}, \njudul: {self.judul}, \npenulis: {self.penulis}, \nkategori: {self.kategori}, \ntahun: {self.tahun}, \nstok: {self.stok}"
    
    def get_data(self):
        return self.data
    
    def load(self):
        self.kode = self.data["kode"]
        self.judul = self.data["judul"]
        self.penulis = self.data["penulis"]
        self.kategori = self.data["kategori"]
        self.tahun = self.data["tahun"]
        self.stok = self.data["stok"]

class Perpus():
    def __init__(self):
        self.daftar_buku = []
        self.load_json()
        self.kategori_tetap = ("Pemrograman", "Jaringan", "Basis Data", "AI")
        self.kategori = None
        self.main()
            
    def load_json(self):
        self.daftar_buku = []
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
            for i in data:
                self.daftar_buku.append(Ebook(i))
            print("-------------------")
            print(">>> Berhasil membaca file <<<")
            print("-------------------")
        except:
            print("-------------------")
            print(">>> Gagal membaca file <<<")
            print("-------------------")
            
    def dump_json(self):
        files = []
        for i in self.daftar_buku:
            files.append(i.get_data())
        try:
            with open("data.json", "w") as f:
                json.dump(files, f, indent=4, sort_keys=True)
            print("-------------------")
            print(">>> Berhasil simpan file <<<")
            print("-------------------")
        except:
            print("-------------------")
            print(">>> Gagal simpan file <<<")
            print("-------------------")
    
    def generator_kode_buku(self):
        total = len(self.daftar_buku) + 1
        kode_buku = f"BK{total:03d}"
        return kode_buku
        
    def main(self):
        self.menu()
        while True:
            if self.cli():
                break

    def menu(self):
        print("****************************")
        print("SISTEM PERPUSTAKAAN DIGITAL")
        print("\nMenu: ")
        print("0. Tambah Buku")
        print("1. Tampilkan Semua Buku")
        print("2. Cari Buku")
        print("3. Urutkan Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Statistik Perpustakaan")
        print("7. Simpan Data")
        print("8. Baca Data")
        print("9. Keluar")
        print("****************************")
        
    def cli(self):
        def tambah_buku():
            print("-------------------")
            print("Masukan data buku")
            print("Biarkan kosong untuk kembali ke menu utama")
            
            print("-------------------\n")
            while True:
                try:
                    judul = input("judul buku: ")
                    penulis = input("penulis buku: ")
                    kategori = input("kategori buku: ")
                    
                    if judul == "" and penulis == "" and kategori == "":
                        print("-------------------")    
                        print(">>> Kembali ke menu utama <<<")
                        print("-------------------")
                        return
                    tahun = int(input("tahun buku: "))
                    stok = int(input("stok buku: "))
                    print()
                except ValueError:
                    print("\n>>> Tahun dan stok harus berbentuk angka <<<")
                    continue
                
                buku = {"kode": self.generator_kode_buku(), "judul": judul,"penulis": penulis,"kategori": kategori,"tahun": tahun,"stok": stok}
                
                buku = Ebook(buku)
                print(buku)
                print("-------------------")    
                print("Apakah data yang di masukan sudah benar?")
                print("-------------------")
                
                hasil = False
                while True:
                    confirmasi = str(input("Y/N: ")).lower()
                    if confirmasi == "y" or confirmasi == "yes":
                        hasil = True
                        break
                    elif confirmasi == "n" or confirmasi == "no":
                        break
                print("-------------------")
                
                if hasil:
                    break
            self.daftar_buku.append(buku)
            print("-------------------")
            print(">>> Berhasil menambahkan buku ke daftar buku <<<")   
            print("-------------------")
            print("****************************")
                
        def tampilkan_buku():
            print("****************************")
            for i in self.daftar_buku:
                print("-------------------")
                print(i)
                print("-------------------")
            print("****************************")

        def cari_buku():
            print("****************************")
            buku_dicari = input("Masukan nama buku: ")
            hasil = None
            for buku in self.daftar_buku:
                if buku.judul.lower() == buku_dicari.lower():
                    hasil = buku
            
            if hasil:
                print("Hasil pencarian: ")
                print()
                print("-------------------")
                print(hasil)
                print("-------------------")
                
            else:
                print("\n>>> Buku tidak di temukan <<<")
            print("****************************")
            
        def urutkan_buku():
            def menu():
                print("****************************")
                print("URUTKAN BERDASARKAN")
                print("\nMenu: ")
                print("0. Judul")
                print("1. Tahun terbit")
                print("2. Stok")
                print("****************************")
                
            def statistik_cli():
                def command_0():
                    self.daftar_buku = sorted(self.daftar_buku, key=lambda buku: buku.judul)
                    print("-------------------")
                    print(f"{len(self.daftar_buku)} buku telah di urutkan berdasarkan judul")
                    print("-------------------") 
                    return True
                    

                def command_1():
                    self.daftar_buku = sorted(self.daftar_buku, key=lambda buku: buku.tahun)
                    print("-------------------")
                    print(f"{len(self.daftar_buku)} buku telah di urutkan tahun")
                    print("-------------------")  
                    return True
                    
                    
                def command_2():
                    self.daftar_buku = sorted(self.daftar_buku, key=lambda buku: buku.stok)
                    print("-------------------")
                    print(f"{len(self.daftar_buku)} buku telah di urutkan stok")
                    print("-------------------")
                    return True
                    
                    
                def command_3():
                    print("-------------------")
                    print(">>> Balik ke menu utama <<<")
                    print("-------------------")
                    return True
                    

                command = input("Command: ")
                print()
                
                match command:
                    case "0":
                        return command_0()
                    case "1":
                        return command_1()
                    case "2":
                        return command_2()
                    case "3":
                        return command_3()
            menu()
            while True:
                if statistik_cli():
                    break
            
        def pinjam_buku():
            print("-------------------")    
            buku_dicari = input("Masukan nama buku: ")
            print("-------------------")    
            
            hasil = None
            for buku in self.daftar_buku:
                if buku.judul.lower() == buku_dicari.lower():
                    hasil = buku
            
            if hasil:
                print("-------------------")
                print(hasil)
                print("-------------------")
                
                meminjam = False
                while True:
                    print("-------------------")    
                    print("Apakah data yang di masukan sudah benar?")
                    print("-------------------")
                    confirmasi = str(input("Y/N: ")).lower()
                    if confirmasi == "y" or confirmasi == "yes":
                        meminjam = True
                        break
                    elif confirmasi == "n" or confirmasi == "no":
                        break
                
                print("-------------------")
                if meminjam and hasil.stok > 0:
                    hasil.stok -= 1
                    print(">>> Berhasil meminjam buku <<<")
                    print(f"stok: {hasil.stok + 1} --> {hasil.stok}")
                elif meminjam and hasil.stok <= 0:
                    print(f'>>> Stok buku "{hasil.judul}" telah habis <<<')
                else:
                    print(">>> Peminjaman di batalkan <<<")
                print("-------------------")    
            else:
 
                print(">>> Buku tidak di temukan <<<")
            print("****************************")
            
        def kembalikan_buku():
            print("-------------------")    
            buku_dicari = input("Masukan nama buku: ")
            print("-------------------")    
            
            hasil = None
            for buku in self.daftar_buku:
                if buku.judul.lower() == buku_dicari.lower():
                    hasil = buku
            
            if hasil:
                print("-------------------")
                print(hasil)
                print("-------------------")
                
                kembalikan = False
                while True:
                    print("-------------------")    
                    print("Apakah data yang di masukan sudah benar?")
                    print("-------------------")
                    confirmasi = str(input("Y/N: ")).lower()
                    if confirmasi == "y" or confirmasi == "yes":
                        kembalikan = True
                        break
                    elif confirmasi == "n" or confirmasi == "no":
                        break
                
                print("-------------------")
                if kembalikan:
                    hasil.stok += 1
                    print(">>> Berhasil kembalikan buku <<<")
                    print(f"stok: {hasil.stok - 1} --> {hasil.stok}")
                else:
                    print(">>> Pengembalian di batalkan <<<")
                print("-------------------")    
            else:
                print(">>> Buku tidak di temukan <<<")
            print("****************************")     
        
        def statistik_perpus():
            semua_penulis = []
            semua_kategori = []
            total_jenis_buku = 0
            stok_ada = []
            stok_habis = []
            total_stok = 0
            
            for buku in self.daftar_buku:
                semua_penulis.append(buku.penulis)
                semua_kategori.append(buku.kategori)
                
                total_stok += int(buku.stok)
                total_jenis_buku += 1
                
                if buku.stok <= 0:
                    stok_habis.append(buku)
                else:
                    stok_ada.append(buku)
            
            def menu():
                print("****************************")
                print("MENU STATISTIK")
                print("\nMenu: ")
                print("0. List semua penulis")
                print("1. List semua kategori")
                print("2. Total jenis buku")
                print("3. Buku yang dalam stok")
                print("4. Buku yang tidak dalam stok")
                print("5. Total stok semua buku")
                print("6. Keluar")
                print("****************************")
            
            def statistik_cli():
                def command_0():
                    print("-------------------")
                    for penulis in sorted(set(semua_penulis)):
                        print(penulis)
                    print("-------------------")    

                def command_1():
                    print("-------------------")
                    for kategori in sorted(set(semua_kategori)):
                        print(kategori)
                    print("-------------------")  
                    
                def command_2():
                    print("-------------------")
                    print(f"Total jenis buku: {total_jenis_buku}")
                    print("-------------------")
                    
                def command_3():
                    print("-------------------")
                    if stok_ada:
                        print(">>> Stock buku yang ada <<<")
                        for buku in stok_ada:
                            print(f"{buku.judul}: {buku.stok}")
                        print("-------------------")  
                    else:
                        print(">>> Semua stok buku habis")
                def command_4():
                    if stok_habis:
                        print("-------------------")
                        print(">>> Stock buku yang habis <<<")
                        for buku in stok_habis:
                            print(f"{buku.judul}: {buku.stok}")
                        print("-------------------")  
                    else:
                        print(">>> Tidak ada stock buku yang habis <<<")

                def command_5():
                    print("-------------------")
                    print(f"Total stok semua buku: {total_stok}")
                    print("-------------------")
                def command_6():
                    print("-------------------")
                    print(">>> Balik ke menu utama <<<")
                    print("-------------------")
                    
                    return True
                    

                command = input("Command: ")
                print()
                
                match command:
                    case "0":
                        command_0()
                    case "1":
                        command_1()
                    case "2":
                        command_2()
                    case "3":
                        command_3()
                    case "4":
                        command_4()
                    case "5":
                        command_5()
                    case "6":
                        return command_6()
            menu()
            while True:
                if statistik_cli():
                    break
                
        def simpan_data():
            self.dump_json()
                
        def baca_data():
            self.load_json()
            
        def keluar():
            print("--------------------")
            print(">>> Terima kasih <<<")    
            print("--------------------")    
            return True
        
        command = input("Command: ")
        print()
        
        match command:
            case "0":
                tambah_buku()
            case "1":
                tampilkan_buku()
            case "2":
                cari_buku()
            case "3":
                urutkan_buku()
            case "4":
                pinjam_buku()
            case "5":
                kembalikan_buku()
            case "6":
                statistik_perpus()
            case "7":
                simpan_data()
            case "8":
                baca_data()
            case "9":
                return keluar()
        
if __name__ == "__main__":
    Perpus()
    
    

#Ini adalah mock data JSON yang digunakan untuk menguji program ini:
[
    {
        "judul": "Cloud Computing Essentials",
        "kategori": "Teknologi",
        "kode": "BK010",
        "penulis": "Jaka",
        "stok": 0,
        "tahun": 2025
    },
    {
        "judul": "Dasar-Dasar Keamanan Siber",
        "kategori": "Keamanan",
        "kode": "BK006",
        "penulis": "Fani",
        "stok": 0,
        "tahun": 2025
    },
    {
        "judul": "Kecerdasan Buatan Terapan",
        "kategori": "AI",
        "kode": "BK009",
        "penulis": "Indah",
        "stok": 2,
        "tahun": 2026
    },
    {
        "judul": "Data Science dengan R",
        "kategori": "Data Science",
        "kode": "BK002",
        "penulis": "Budi",
        "stok": 3,
        "tahun": 2023
    },
    {
        "judul": "Python Dasar",
        "kategori": "Pemrograman",
        "kode": "BK001",
        "penulis": "Andi",
        "stok": 5,
        "tahun": 2024
    },
    {
        "judul": "Belajar React Native",
        "kategori": "Pemrograman",
        "kode": "BK005",
        "penulis": "Eka",
        "stok": 6,
        "tahun": 2024
    },
    {
        "judul": "Manajemen Proyek IT",
        "kategori": "Bisnis",
        "kode": "BK008",
        "penulis": "Hani",
        "stok": 7,
        "tahun": 2023
    },
    {
        "judul": "Desain UI/UX Modern",
        "kategori": "Desain",
        "kode": "BK003",
        "penulis": "Citra",
        "stok": 8,
        "tahun": 2025
    },
    {
        "judul": "Pengembangan Web dengan PHP",
        "kategori": "Pemrograman",
        "kode": "BK007",
        "penulis": "Gani",
        "stok": 10,
        "tahun": 2021
    },
    {
        "judul": "Algoritma dan Struktur Data",
        "kategori": "Ilmu Komputer",
        "kode": "BK004",
        "penulis": "Dedi",
        "stok": 12,
        "tahun": 2022
    }
]