import sys 
import os

cwd = os.getcwd()
try:
    sys.argv[1]
except:
    exec(open('./module/noArgs.py'))
    sys.exit()

args = sys.argv[1]
if (args == 'build'):
    try :
        sys.argv[2]
    except :
        print('masukan nama file yang akan di eksekusi')
        sys.exit()
    path = cwd + '/' + sys.argv[2]
    with open(path, 'r') as f:
        first_line = f.readline().strip('\n')
        if (first_line == 'utama' or first_line == 'main'):
            os.system("python3 " + './module/exec/build.py ' + path)
            sys.exit()
        else :
            print('file =>> "' + sys.argv[2] + '" <<= tidak teridentifikasi sebagai file gabut yang utama')
            print('baris pertamanya adalah =>> ' + first_line)
if (args == 'listen'):
    try :
        sys.argv[2]
    except :
        print('masukan direktori yang akan di pantau')
        sys.exit()
    print('Memantau direktori...')
    path = cwd + '/' + sys.argv[2]
    