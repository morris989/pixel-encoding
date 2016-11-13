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
        f.write(b''+chr(i[0]))
    f.close()
    print "Done."

# Todo: offset x,y OPTIMIZE FOR BIG FILES
# lenght, direction    
def encode(input,output):
    """encode message"""
    f=open(input,"rb")
    ar=[]
    size=0
    for row in f:
        for char in row:
            ar.append(ord(char))
            size+=1
    x=size/2
    y=x
    f.close()
    im=Image.new("RGB",(x,y),"white")
    for i in xrange(y):
        for j in xrange(x):
            if i*(x)+(j)>size-1:
                continue
            im.putpixel((j,i),(ar[i*(x)+(j)],0,0))
    im.save(output, format='BMP')
    print("Done")
            
# Todo: Beautify
def usage():
    print "[*] pixel-encoding 'mode' input output "
    print "[*] Specifi mode encode -e(Not implemented) or decode -d "

# Todo: Validations, execption optimization
def main():
    input=""
    output=""
    mode=""
    if len(argv)!=4:
        usage()
    else:
        input=argv[2]
        output=argv[3]
        mode=argv[1]
    if mode == "-d":
        decode(input,output)
    elif mode=="-e":
        encode(input,output)
    else:
        print "No implementado."
 
if __name__ == '__main__':
    main()
