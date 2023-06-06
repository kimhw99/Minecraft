from PIL import Image
#Read Images
def singleChest(inputImage, outputImage):
    image = Image.open(inputImage) # single chest
    image_size = image.size

    dim = int((image.size[0]/4)*0.875)
    lid  = int(5 * (dim/14))
    base  = int(10 * (dim/14))
    lock = int(dim/14)

    lock0 = image.crop((lock, 0, 3*lock, lock)).transpose(Image.ROTATE_180)
    lock1 = image.crop((3*lock, 0, 5*lock, lock)).transpose(Image.ROTATE_180)

    lock2 = image.crop((0, lock, lock, 5*lock)).transpose(Image.ROTATE_180)
    lock3 = image.crop((lock, lock, lock*3, 5*lock)).transpose(Image.ROTATE_180)
    lock4 = image.crop((lock*3, lock, lock*4, 5*lock)).transpose(Image.ROTATE_180)
    lock5 = image.crop((lock*4, lock, lock*6, 5*lock)).transpose(Image.ROTATE_180)

    lidBottom = image.crop((dim, 0, dim*2, dim)).transpose(Image.FLIP_TOP_BOTTOM)
    lidTop = image.crop((dim*2, 0, dim*3, dim)).transpose(Image.FLIP_TOP_BOTTOM)

    lidLeft = image.crop((0, dim, dim, dim + lid)).transpose(Image.ROTATE_180)
    lidBack = image.crop((dim, dim, dim*2, dim + lid)).transpose(Image.ROTATE_180)
    lidRight = image.crop((dim*2, dim, dim*3, dim + lid)).transpose(Image.ROTATE_180)
    lidFront = image.crop((dim*3, dim, dim*4, dim + lid)).transpose(Image.ROTATE_180)

    baseBottom = image.crop((dim, dim + lid, dim*2, dim*2 + lid)).transpose(Image.FLIP_TOP_BOTTOM)
    baseTop = image.crop((dim*2, dim + lid, dim*3, dim*2 + lid)).transpose(Image.FLIP_TOP_BOTTOM)

    baseLeft = image.crop((0, dim*2 + lid, dim, dim*2 + lid + base)).transpose(Image.ROTATE_180)
    baseBack = image.crop((dim, dim*2 + lid, dim*2, dim*2 + lid + base)).transpose(Image.ROTATE_180)
    baseRight = image.crop((dim*2, dim*2 + lid, dim*3, dim*2 + lid + base)).transpose(Image.ROTATE_180)
    baseFront = image.crop((dim*3, dim*2 + lid, dim*4, dim*2 + lid + base)).transpose(Image.ROTATE_180)

    #baseTop.show()

    #chest
    #new_image = Image.new(mode = "RGBA", size = (image.size[0], image.size[0]), color = (255, 255, 255, 0))

    image.paste(lidTop, (dim, 0))
    image.paste(lidBottom, (dim*2, 0))

    image.paste(lidLeft, (0, dim))
    image.paste(lidFront, (dim, dim))
    image.paste(lidRight, (dim*2, dim))
    image.paste(lidBack, (dim*3, dim))

    image.paste(baseTop, (dim, dim + lid))
    image.paste(baseBottom, (dim*2, dim + lid))

    image.paste(baseLeft, (0, dim*2 + lid))
    image.paste(baseFront, (dim, dim*2 + lid))
    image.paste(baseRight, (dim*2, dim*2 + lid))
    image.paste(baseBack, (dim*3, dim*2 + lid))

    image.paste(lock0, (3*lock, 0))
    image.paste(lock1, (lock, 0))

    image.paste(lock2, (0, lock))
    image.paste(lock3, (lock*4, lock))
    image.paste(lock4, (lock*3, lock))
    image.paste(lock5, (lock, lock))

    image.save(outputImage,"PNG")

# 28
# 10 + 20
# ------------------------------------------------------

def doubleChest(inputNameLeft, inputNameRight, outputName):
    image1 = Image.open(inputNameLeft) # double chest
    image2 = Image.open(inputNameRight) 
    image_size = image2.size

    dim = int((image1.size[0]/4)*0.875)
    lid  = int(5 * (dim/14))
    base  = int(10 * (dim/14))
    lock = int(dim/14)

    lidTop1 = image1.crop((dim*2 + lock, 0, dim*3 + lock*2, dim)).transpose(Image.FLIP_TOP_BOTTOM)
    lidTop2 = image2.crop((dim*2 + lock, 0, dim*3 + lock*2, dim)).transpose(Image.FLIP_TOP_BOTTOM)

    lidBottom1 = image1.crop((dim, 0, dim*2 + lock*1, dim))
    lidBottom2 = image2.crop((dim, 0, dim*2 + lock*1, dim))

    lidFront1 = image1.crop((dim*3 + lock*1, dim, dim*4 + lock*2, dim + lid)).transpose(Image.ROTATE_180)
    lidFront2 = image2.crop((dim*3 + lock*1, dim, dim*4 + lock*2, dim + lid)).transpose(Image.ROTATE_180)

    lidLeft = image1.crop((dim*2 + lock, dim, dim*3 + lock*2, dim + lid)).transpose(Image.ROTATE_180)
    lidRight = image2.crop((0, dim, dim, dim + lid)).transpose(Image.ROTATE_180)

    lidBack1 = image1.crop((dim, dim, 2*dim + lock, dim + lid)).transpose(Image.ROTATE_180)
    lidBack2 = image2.crop((dim, dim, 2*dim + lock, dim + lid)).transpose(Image.ROTATE_180)

    baseFront1 = image1.crop((dim*3 + lock, dim*2 + lid, dim*4 + lock*2, dim*2 + lid + base)).transpose(Image.ROTATE_180)
    baseFront2 = image2.crop((dim*3 + lock, dim*2 + lid, dim*4 + lock*2, dim*2 + lid + base)).transpose(Image.ROTATE_180)

    baseTop1 = image1.crop((dim*2 + lock, dim + lid, dim*3 + lock*2, dim*2 + lid)).transpose(Image.FLIP_TOP_BOTTOM)
    baseTop2 = image2.crop((dim*2 + lock, dim + lid, dim*3 + lock*2, dim*2 + lid)).transpose(Image.FLIP_TOP_BOTTOM)

    baseLeft = image1.crop((dim*2 + lock, dim*2 + lid, dim*3 + lock, dim*2 + lid + base)).transpose(Image.ROTATE_180)
    baseRight = image2.crop((0, dim*2 + lid, dim, dim*2 + lid + base)).transpose(Image.ROTATE_180)

    baseBack1 = image1.crop((dim, dim*2 + lid, dim*2 + lock, dim*2 + lid + base)).transpose(Image.ROTATE_180)
    baseBack2 = image2.crop((dim, dim*2 + lid, dim*2 + lock, dim*2 + lid + base)).transpose(Image.ROTATE_180)

    baseBottom1 = image1.crop((dim, dim + lid, dim*2 + lock, dim*2 + lid))
    baseBottom2 = image2.crop((dim, dim + lid, dim*2 + lock, dim*2 + lid))

    lock0a = image2.crop((lock,0, lock*2, lock)).transpose(Image.ROTATE_180)
    lock1a = image1.crop((lock,0, lock*2, lock)).transpose(Image.ROTATE_180)
    lock0b = image2.crop((lock*2,0, lock*3, lock)).transpose(Image.ROTATE_180)
    lock1b = image1.crop((lock*2,0, lock*3, lock)).transpose(Image.ROTATE_180)


    lock2 = image2.crop((0, lock, lock, lock*5)).transpose(Image.ROTATE_180)

    lock3b = image2.crop((lock, lock, lock*2, lock*5)).transpose(Image.ROTATE_180)
    lock3a = image1.crop((lock, lock, lock*2, lock*5)).transpose(Image.ROTATE_180)

    lock4 = image1.crop((lock*2, lock, lock*3, lock*5)).transpose(Image.ROTATE_180)

    lock5a = image2.crop((lock*3, lock, lock*4, lock*5)).transpose(Image.ROTATE_180)
    lock5b = image1.crop((lock*3, lock, lock*4, lock*5)).transpose(Image.ROTATE_180)

    # paste
    image = Image.new(mode = "RGBA", size = (int(image1.size[0]*2), image1.size[0]), color = (255, 255, 255, 0))

    image.paste(lidTop1, (dim*2 + lock, 0))
    image.paste(lidTop2, (dim, 0))

    image.paste(lidBottom1, (dim*4 + lock*3, 0))
    image.paste(lidBottom2, (dim*3 + lock*2, 0))

    image.paste(lidFront1, (dim*2 + lock, dim))
    image.paste(lidFront2, (dim, dim))

    image.paste(lidLeft, (dim*3 + lock*1, dim))
    image.paste(lidRight, (0, dim))

    image.paste(lidBack1, (dim*4 + lock*2, dim))
    image.paste(lidBack2, (dim*5 + lock*3, dim))

    image.paste(baseFront1, (dim*2 + lock, dim*2 + lid))
    image.paste(baseFront2, (dim, dim*2 + lid))

    image.paste(baseTop1, (dim*2 + lock, dim + lid))
    image.paste(baseTop2, (dim, dim + lid))

    image.paste(baseLeft, (dim*3 + lock*2, dim*2 + lid))
    image.paste(baseRight, (0, dim*2 + lid))

    image.paste(baseBack1, (dim*4 + lock*2, dim*2 + lid))
    image.paste(baseBack2, (dim*5 + lock*3, dim*2 + lid))

    image.paste(baseBottom1, (dim*4 + lock*3, dim + lid))
    image.paste(baseBottom2, (dim*3 + lock*2, dim + lid))

    image.paste(lock0b, (lock,0))
    image.paste(lock1b, (lock*2,0))
    image.paste(lock0a, (lock*3,0))
    image.paste(lock1a, (lock*4,0))

    image.paste(lock2, (0, lock))
    image.paste(lock5a, (lock, lock))
    image.paste(lock5b, (lock*2, lock))
    image.paste(lock4, (lock*3, lock))
    image.paste(lock3a, (lock*4, lock))
    image.paste(lock3b, (lock*5, lock))

    image.save(outputName,"PNG")

print("}")

for i in ["christmas.png", 'ender.png', 'normal.png', 'trapped.png']:
    if os.path.isfile(i) is True:
        singleChest(i,i)

#singleChest('ender.png','ender.png')
#singleChest('normal.png','normal.png')
#singleChest('trapped.png','trapped.png')

for i in ["christmas", 'normal', 'trapped']:
    if os.path.isfile(i+"_left.png") is True:
        if os.path.isfile(i+"_right.png") is True:
            doubleChest(i+"_left.png", i+"_right.png", i+"_double.png")

        #doubleChest('normal_left.png', 'normal_right.png', 'normal_double.png')
        #doubleChest('trapped_left.png', 'trapped_right.png', 'trapped_double.png')



