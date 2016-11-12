from PIL import Image
from sys import argv

# Todo: offset x,y
# lenght, direction
def decode(input,output):
    """decode message"""
    ar=[]
    im=Image.open(input)
    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            ar.append(im.getpixel((x,y)))
    im.close()
    f=open(output,"wb")
    for i in ar:
        f.write(b''+chr(i))
    f.close()
    print "Done."

def use_help():
    print "[*] pixel-encoding 'mode' input output "
    print "[*] Specifi mode encode -e(Not implemented) or decode -d "
    
def main():
    input=""
    output=""
    mode=""
    if len(argv)!=4:
        use_help()
    else:
        input=argv[2]
        output=argv[3]
        mode=argv[1]
    if mode == "-d":
        decode(input,output)
    else:
        print "No implementado."
 
if __name__ == '__main__':
    main()