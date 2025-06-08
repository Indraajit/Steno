import steno
import pyfiglet
from rich.console import Console

console = Console()

def createBanner(title, font):
    asciiArt = pyfiglet.figlet_format(title, font=font)
    console.print(asciiArt, style='bold blue')

def excuteStenography(mode):
    steno.createDirectory()
    if mode.lower() == "comp":
        zipfile = str(input('[*] Enter Zipfile Name : ')).strip().lower()
        image = str(input("[*] Enter Image File Name (eg: hello.jpg): ")).strip()
        out = str(input("[*] Enter Steno File Name (eg: hello.jpg): ")).strip()
        steno.createZipFiles(zipfile, 'files')
        steno.compileIntoBinary(image, zipfile +'.zip', out)
        console.print("[+] Files are converted into Images", style='bold green')
    elif mode.lower() == 'decomp':
        image = str(input("[*] Enter Steno Image(eg: hello.jpg): ")).strip()
        zipfile = str(input('[*] Enter Zipfile Name : ')).strip()
        steno.decompileIntoZip(image, zipfile +'.zip')
        console.print("[+] Image are converted into Files", style='bold green')

def getInputs():
    createBanner('stenoGraphy', 'doom')
    mode = str(input("Enter Mode (comp or decomp) : ")).strip()
    excuteStenography(mode)

getInputs()