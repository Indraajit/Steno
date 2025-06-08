import os
import shutil
import subprocess

def createDirectory():
    if not os.path.exists('files'):
        os.makedirs('files')

def createZipFiles(zipfile, path):
    shutil.make_archive(zipfile, 'zip', path)

def compileIntoBinary(imagefile, zipfile, outputfile):
    command = f'copy /b "{imagefile}"+"{zipfile}" "{outputfile}"'
    delCommand = f'del "{imagefile}" "{zipfile}"'
    subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(delCommand, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def decompileIntoZip(imagefile, outputfile):
    command = f'copy "{imagefile}" "{outputfile}"'
    delCommand = f'del "{imagefile}"'
    subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(delCommand, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)