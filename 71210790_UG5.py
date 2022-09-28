from pickle import NONE


class Karyawan:
    _nama = ""
    _umur = ""
    _jenisKelamin = NONE
    _upahPerHari = NONE

    def __init__(self, nama, umur, jenisKelamin, upahPerHari):
        self._nama = nama
        self._umur = umur
        self._jenisKelamin = jenisKelamin
        self._upahPerHari = upahPerHari

    def setNama(self,nama):
        self._nama = nama

    def setUmur(self,umur):
        self._umur = umur

    def setJenisKelamin(self,jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def setUpahPerHari(self,upahPerhari):
        self._upahPerHari = upahPerhari

    def printInfo(self):
        print("Nama :", self._nama)
        print("Umur :", self._umur)
        print("Jenis Kelamin :", self._jenisKelamin)
        print("Upah Perhari :", self._upahPerHari)

    def hitungGajiBulanan(self,tiapHari):
        if self._upahPerHari  == None  or self._jenisKelamin == None:
            print ("EROR! Kapasitas BBM atau Jenis Bahan Bakar belum diinputkan")
        else :   
            print("Mengisi :",self.setUpahPerHari())
            print("Total Harga :",self.setUpahPerHari()*tiapHari)

if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90,None,None)
    orang1.printInfo()
    orang2 = Karyawan("Sindu", 190,None,None)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()
    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)