import zipfile
import sys
import os
from threading import Thread

# Command line error handling
if len(sys.argv) < 3:
    sys.exit('Zip password cracker, usage: %s <zipped_file_to_crack> <dictionary_path>' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: ZIP file %s was not found!' % sys.argv[1])
elif not os.path.exists(sys.argv[2]):
    sys.exit('ERROR: %s was not found!' % sys.argv[2])

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password: '+password+'\n'
    except:
        pass

def main():
    zFile = zipfile.ZipFile(sys.argv[1])
    passFile = open(sys.argv[2])

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
