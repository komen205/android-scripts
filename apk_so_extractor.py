import zipfile
import os
import sys

#This script will extract the libraries of an apk
path = sys.argv[1]

if path is None:
    print("please input the absolute path of the apk")


archive = zipfile.ZipFile(path)

for file in archive.namelist():
    if file.startswith('lib/'):
        archive.extract(file, 'extracted_libs')

print("libs were extracted")