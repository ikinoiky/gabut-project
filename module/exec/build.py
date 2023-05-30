import sys, re

cache = dict()
f = open(sys.argv[1], 'r')
kata = ['adalah ', 'fungsi ', 'kelas ', 'tuliskan ', 'jika ']
var = []
lanjut = True
lanjut_key = ""
lanjut_line_before = ""
lanjut_value = ""
l = 0

for line in f:
    if lanjut is True:
        if line.find(kata[0]) != -1:
            setvar = line.split(kata[0])[-2].replace(" ","")
            var.append(setvar)
            lanjut_value += line.split(kata[0])[1].replace("\n", "")
            if line.split(kata[0])[1].find(',') != -1:
                lanjut = False
                lanjut_key = 'variabel'
                lanjut_line_before = l
            else:
                cache[setvar] = line.split(kata[0])[1].replace("\n", "")
        if lanjut == True:
            if line.find(kata[3]) != -1:
                if line.split(kata[3])[1].find('apa itu ') != -1:
                    getvar = line.split(kata[3])[1].replace('apa itu ', "").replace('\n', "")
                    print(getvar, 'adalah', cache[getvar])
                else:
                    getvar = line.split(kata[3])[1].replace('\n', "")
                    print(cache[getvar])
    else:
        if line.rfind('.') != -1:
            if line.split('.')[1].replace("\n", "") != '':
                print('tidak boleh ada huruf setelah titik')
            else:
                lanjut_value += line.replace('.', "").replace('\n',"")
                lanjut = True
                cache[setvar] = lanjut_value.replace("\n", "").replace(',', ' ')
        else:
            lanjut_value += line
                

    l += 1
