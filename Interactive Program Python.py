#Program Interaksi Saling Menyerang
class pahlawan:

    def __init__ (self, nama, kesehatan, kekuatan):
        self.nama = nama
        self.kesehatan = kesehatan
        self.kekuatan = kekuatan
    
    def serang(self, pahlawan):
        print(self.nama + ' menyerang ' + 'sebanyak ' + str(pahlawan.kesehatan))
        pahlawan.diserang()
        pahlawan.menyerang1(self, self.kekuatan)
    
    def diserang (self):
        print(self.nama + ' sedang diserang')

    def menyerang1(self, pahlawan, kekuatan_lawan):
        print(self.nama + ' menyerang balik ' + pahlawan.nama )
        serangan_diterima = kekuatan_lawan * self.kekuatan
        print('serangan terasa ' + str(serangan_diterima))
        self.kesehatan -= serangan_diterima
        print('darah ' + self.nama + ' tersisa ' +str(self.kesehatan))

antonio = pahlawan('antonio', 100, 20)
karim = pahlawan ('karim', 200, 30)

antonio.serang(karim)
print('\n')
karim.serang(antonio)