import zipfile
import os
import sys

#This script will extract the libraries of an apk
path = sys.argv[1]

if path is None:
    print("please input the absolute path of the apk")


archive = zipfile.ZipFile(path)

with archive as zip_ref:
    zip_ref.extractall("apk")

print("libs were extracted")