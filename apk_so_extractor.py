import zipfile
import os

with zipfile.ZipFile("app-release.apk", 'r') as zip_ref:
    zip_ref.extractall('lib')