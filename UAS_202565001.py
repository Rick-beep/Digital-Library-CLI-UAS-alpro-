'''


Github: https://github.com/Rick-beep
'''

import json
class Ebook():
    def __init__(self, data_dic):
        self.data = data_dic
        self.load()
    
    def __str__(self):
        return f"kode: {self.kode}, judul: {self.judul}, penulis: {self.penulis}, kategori: {self.kategori}, tahun: {self.tahun}, stok: {self.stok}"
    
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
        self.main()
        
    def main(self):
        pass

if __name__ == "__main__":
    pass


{
"kode": "BK001",
"judul": "Python Dasar",
"penulis": "Andi",
"kategori": "Pemrograman",
"tahun": 2024,
"stok": 5
}