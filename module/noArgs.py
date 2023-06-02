import sys, re

class syntax:
    def __init__(self) -> None:
        pass
    def kata(self, kata):
        # main 
        if kata == 'Main' or kata == 'utama':
            self.kataMain()
        # variabel 
        if kata == 'Adalah' or kata == '=':
            self.kataVariable()
        # kelas
        if kata == 'Kelas':
            self.kataKelas()
        # fungsi 
        if kata == 'Fungsi' or kata == 'func' or kata == 'fungi':
            self.kataFunc()
        # jika 
        if kata == 'Jika':
            self.kataJika()
        # exec function
        if kata == '()':
            print(kata)
            self.execFunc()

    def kataMain():
        print('main')

    def kataVariable():
        print('variable')

    def kataKelas():
        print('kelas')

    def kataJika():
        print('jika')

    def kataFunc():
        print('fungsi')

    def execFunc():
        print('execFungsi')
    
    def cariKata(self, line):
        for word in line.split():
            print('test')

    def bacaFile(self):
        for line in file:
            self.cariKata(self, line)

file = sys.argv[1]
file = open(file)
print(repr(file.read()).replace("    ", "\\t")) 

with file as f:
    first_line = f.readline().strip('\n').replace(" ", "")
    if (first_line == 'Utama' or first_line == 'Main'):
        syntax.bacaFile(syntax)
    else:
        print('file =>> "' + sys.argv[1] + '" <<= tidak teridentifikasi sebagai file gabut yang utama')
        print('baris pertamanya adalah =>> ' + first_line)

