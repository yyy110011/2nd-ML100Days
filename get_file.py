import requests
import os
import zipfile
import sys
def download_pack(url, path, name):
    r = requests.get(url)
    with open(os.path.join(path, name + '.7z'), 'wb') as f:
        f.write(r.content)
    f.close()


    
    zip_ref = zipfile.ZipFile(os.path.join(path, name + '.7z'), 'r')
    zip_ref.extractall(os.path.join(path, name))
    zip_ref.close()








if __name__ == "__main__":
    a = sys.argv[1]
    a = a.split(' ')
    print(a)
    download_pack(a[0], a[1], a[2])