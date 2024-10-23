#Ibadurrohman Al-Fath
class perpustakaan:
    def __init__(self, name):
       self.name=name
       self.__buku = []
    def tambah_buku(self, buku):
       self.__buku.append(buku)
    def tampilkan_buku(self):
       for buku in self._buku:
        print(buku.info())
    def __str__(self):
        return f"perpustakaan:{self.name}"
    
class buku:
    def __init__(self, judul,penulis):
       self.judul = judul
       self.penulis= penulis
    def info(self):
       return f"buku:{self.judul}oleh{self.penulis}"
   
class buku_fiksi(buku):
    def __init__(self,judul,penulis,genre):
       super().__init__(judul,penulis)
       self.genre = genre
    def info(self):
       return f"buku fiksi: {self.judul}oleh{self.penulis}, genre: {self.genre}"
   
class bukunonfiksi(buku):
    def __init__(self,judul,penulis,topik):
        super().__init__(judul,penulis)
        self.topik = topik
    def info(self):
        return f"bukunonfiksi:{self.judul}oleh{self.penulis},topik:{self.topik}"
                    
perpustakaan = perpustakaan("perpustakaan kota")

buku1 = buku_fiksi("harry potter", "j.k rowling","fantasi")
buku2 = bukunonfiksi("sapiens", "yuval noah harari","sejarah")
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
print(perpustakaan)
perpustakaan.tampilkan_buku()                   
    
       
    
       
       