'''
Christian Gilbert Rusianto (202565001)
https://github.com/Rick-beep
'''

import json
class Ebook():
    def __init__(self, data_dic):
        self.data = data_dic
        self.load()
    
    def __str__(self):
        return f"kode: {self.kode}, \njudul: {self.judul}, \npenulis: {self.penulis}, \nkategori: {self.kategori}, \ntahun: {self.tahun}, \nstok: {self.stok}\n"
    
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
        self.buku_buku = []
        self.load_json()
        self.main()
        
    def main(self):
        self.cmd_list()
        while True:
            self.cli()
            
    def load_json(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        for i in data:
            self.buku_buku.append(Ebook(i))
            
    def dump_json():
        pass
    
    def cmd_list(self):
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
        def command_0():
            pass
        def command_1():
            pass
        def command_2():
            pass
        def command_3():
            pass
        def command_4():
            pass        
        def command_5():
            pass        
        def command_6():
            pass        
        def command_7():
            pass        
        def command_8():
            pass
        def command_9():
            pass 
        
        command = input("Command: ")
        print()
        
        match command:
            case "0":
                pass
            case "1":
                print("****************************")
                for i in self.buku_buku:
                    print(i)
                print("****************************")
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
        

if __name__ == "__main__":
    Perpus()


{
"kode": "BK001",
"judul": "Python Dasar",
"penulis": "Andi",
"kategori": "Pemrograman",
"tahun": 2024,
"stok": 5
}