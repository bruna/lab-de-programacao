import sys
abre = open(sys.argv[1], "r")
fecha = open(sys.argv[2], "w")

retA = abre.readline()
retA = retA.split()
retB = abre.readline()
retB = retB.split()
ax1=float(retA[0])
ay1=float(retA[1])
ax2=float(retA[2])
ay2=float(retA[3])
bx1=float(retB[0])
by1=float(retB[1])
bx2=float(retB[2])
by2=float(retB[3])

if ax1<bx1:
    if ax2>bx1:
        if ay1<by1:
            if ay2>=by1:
                colide="1"
            else:
                colide="0"
        else:
            if ay1<=by2:
                colide="1"
            else:
                colide="0"
    else:
        colide="0"
else:
    if ax1<=bx2:
        if ay1<by1:
            if ay2>=by1:
                colide="1"
            else:
                colide="0"
        else:
            if ay1<=by2:
                colide="1"
            else:
                colide="0"
    else:
        colide="0"

fecha.write(colide + "\n")
fecha.close()
abre.close()
