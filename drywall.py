from math import *


"""this determines the number of sheets required to cover the walls """
def sheetsrequired(width,depth,sheetsize):
    w = (width/sheetsize[0])
    if w % 1 != 0:
        w += 1
    w = int(w)
    #print(w)

    x = (depth/sheetsize[1])
    if x % 1 != 0:
        x += 1
    x = int(x)
    #print(x)

    y = (width/sheetsize[1])
    if y % 1 != 0:
        y += 1
    y = int(y)
    #print(y)

    z = (depth/sheetsize[0])
    if z % 1 != 0:
        z += 1
    z = int(z)
    #print(z)

    if (w * x) >= (y * z):
        return (y * z)
        ret = y * z
        #print(ret)
    else:
        return (w * x)
        ret2 = w * x
        #print(ret2)

def drywall_sheets_required(width,depth,height,sheetSize=(4,8),useScrap=True):
    if useScrap:
        a = (width * depth + 2 * (width + depth) * height) / (sheetSize[0] * sheetSize[1])
        if a % 1 != 0:
            a += 1
        else:
            a = int(a)
            print("using scrap, the number of drywall sheets is: ",a)
            return a
            
    else:
        print("without using scrap, the number of drywall sheets is: ",sheetsrequired(width,depth,sheetSize) + (sheetsrequired(width,height,sheetSize) + sheetsrequired(depth,height,sheetSize)) * 2)
        return sheetsrequired(width,depth,sheetSize) + (sheetsrequired(width,height,sheetSize) + sheetsrequired(depth,height,sheetSize)) * 2
        
drywall_sheets_required(12,16,8,sheetSize=(4,8),useScrap=True)
drywall_sheets_required(12,16,8,sheetSize=(4,8),useScrap=False)
