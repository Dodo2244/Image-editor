import msvcrt
from time import sleep
from os import system
def main():
    choice = int(input("1: 4 x 4\n2: 8 x 8\n3: 20 x 20\nChoice: "))
    height = 0
    width = 0
    if choice == 1:
        height = 4
        width = 4
    elif choice == 2:
        height = 8
        width = 8
    elif choice == 3:
        height = 20
        width = 20
    else:
        print("Invalid")
        sleep(0.5)
        exit = 1


    file = open("Newphoto.bmp","wb")
    addSig(choice,file)
    writePixels(file,height,width)
    file.close()

def addSig(choice,file):
    if choice == 1:
        sigFile = open("4","rb")
        _tmp = sigFile.read(54)
        file.write(_tmp)
        
    if choice == 2:
        sigFile = open("8","rb")
        _tmp = sigFile.read(54)
        file.write(_tmp)

    if choice == 3:
        sigFile = open("20","rb")
        _tmp = sigFile.read(54)
        file.write(_tmp)

        
def writePixels(file,height,width):
    system("cls")
    white = bytearray([0xff,0xff,0xff])
    black = bytearray([0x00,0x00,0x00])
    for i in range(height):
        for j in range(width):
            inpt = msvcrt.getche()
            color = chr(inpt[0])
            if color == '0':
                file.write(white)
            elif color == 'b':
                file.write(black)
        print("")

if __name__ == "__main__":
    main()
