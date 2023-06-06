from PIL import Image
#clock
if os.path.isfile("clock_00.png") is True:
    image = Image.open('clock_00.png').convert("RGBA")
    image_size = image.size

    new_image = Image.new(mode = "RGBA", size = (image.size[0], image.size[0]*64), color = (255, 255, 255, 0))

    for i in range(0, 64):
        num = str(i)
        if len(num) ==1:
            num = "0" + num
        image = Image.open('clock_' + num + '.png').convert("RGBA")
        new_image.paste(image, (0, i*image_size[0]), image)

    new_image.save("clock.png","PNG")

#compass
if os.path.isfile("compass_00.png") is True:
    image = Image.open('compass_00.png').convert("RGBA")
    image_size = image.size
    
    new_image = Image.new(mode = "RGBA", size = (image.size[0], image.size[0]*32), color = (255, 255, 255, 0))

    for i in range(0, 32):
        num = str(i)
        if len(num) ==1:
            num = "0" + num
        image = Image.open('compass_' + num + '.png').convert("RGBA")
        new_image.paste(image, (0, i*image_size[0]), image)

    new_image.save("compass.png","PNG")
