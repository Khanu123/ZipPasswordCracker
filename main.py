import zipfile

def extractFile(zipped_file, password):
    try:
        zipped_file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('Incorrect password')
        return

def main():
    zfile = zipfile.ZipFile('test.zip')
    passFile = open('passlist.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print('Password = ' + password)
            break

if __name__ == '__main__':
    main()
