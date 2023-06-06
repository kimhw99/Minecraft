from PIL import Image
#Read Images
image = Image.open('alban.png')
size = int(image.size[0])

new_image = Image.new(mode = "RGBA", size = (size * 16, size * 16), color = (255, 255, 255, 0))

new_image.paste(Image.open('kebab.png'),(0,0))
new_image.paste(Image.open('aztec.png'),(size,0))
new_image.paste(Image.open('alban.png'),(size*2,0))
new_image.paste(Image.open('aztec2.png'),(size*3,0))
new_image.paste(Image.open('bomb.png'),(size*4,0))
new_image.paste(Image.open('plant.png'),(size*5,0))
new_image.paste(Image.open('wasteland.png'),(size*6,0))

new_image.paste(Image.open('pool.png'),(0,size*2))
new_image.paste(Image.open('courbet.png'),(size*2,size*2))
new_image.paste(Image.open('sea.png'),(size*4,size*2))
new_image.paste(Image.open('sunset.png'),(size*6,size*2))
new_image.paste(Image.open('creebet.png'),(size*8,size*2))

new_image.paste(Image.open('wanderer.png'),(0,size*4))
new_image.paste(Image.open('graham.png'),(size*1,size*4))
new_image.paste(Image.open('skeleton.png'),(size*12,size*4))

new_image.paste(Image.open('fighters.png'),(0,size*6))
new_image.paste(Image.open('donkey_kong.png'),(size*12,size*7))

new_image.paste(Image.open('match.png'),(0,size*8))
new_image.paste(Image.open('bust.png'),(size*2,size*8))
new_image.paste(Image.open('stage.png'),(size*4,size*8))
new_image.paste(Image.open('void.png'),(size*6,size*8))
new_image.paste(Image.open('skull_and_roses.png'),(size*8,size*8))
new_image.paste(Image.open('wither.png'),(size*10,size*8))

new_image.paste(Image.open('pointer.png'),(0,size*12))
new_image.paste(Image.open('pigscene.png'),(size*4,size*12))
new_image.paste(Image.open('burning_skull.png'),(size*8,size*12))

for i in range(0, 4):
    for j in range(0, 4):
        new_image.paste(Image.open('back.png'),(size*(12+i),size*j))

new_image.save('paintings_kristoffer_zetterstrand.png')
