from PIL import Image
#Read Images
image = Image.open('map_icons.png')
size = int(image.size[0] /4)
icon = int(size / 4)

row1 = image.crop((0,0,size,icon))
row2 = image.crop((size,0,size*2,icon))

new_image = Image.new(mode = "RGBA", size = (size, size), color = (255, 255, 255, 0))
new_image.paste(row1,(0,0))
new_image.paste(row2, (0,icon))

new_image.save('map_icons.png')
