from PIL import Image
import os
#Read Images

size = 8 #temp

if os.path.isfile('critical_hit.png') is True:
    image = Image.open('critical_hit.png')
    size = int(image.size[0])

elif os.path.isfile('generic_0.png') is True:
    image = Image.open('generic_0.png')
    size = int(image.size[0])

new_image = Image.open('particles.png').resize((size*16, size*16), Image.Resampling.NEAREST)

ench = 'abcdefghijklmnopqrstuvwxyz'



if os.path.isfile('generic_0.png') is True:
    for i in range(0, 7):
        new_image.paste(Image.open('generic_'+str(i)+'.png').resize((size, size), Image.Resampling.NEAREST),(size*i, 0))

if os.path.isfile('splash_0.png') is True:
    new_image.paste(Image.open('splash_0.png').resize((size, size), Image.Resampling.NEAREST),(0, size))

    for i in range(3, 7):
        new_image.paste(Image.open('splash_'+str(i-3)+'.png').resize((size, size), Image.Resampling.NEAREST),(size*i, size))

if os.path.isfile('bubble.png') is True:
    new_image.paste(Image.open('bubble.png').resize((size, size), Image.Resampling.NEAREST),(0, size*2))

if os.path.isfile('fishing_hook.png') is True:
    new_image.paste(Image.open('fishing_hook.png').resize((size, size), Image.Resampling.NEAREST),(size, size*2))

if os.path.isfile('flash.png') is True:
    new_image.paste(Image.open('flash.png').resize((size*4, size*4), Image.Resampling.NEAREST),(size*4, size*2))
    
if os.path.isfile('flame.png') is True:
    new_image.paste(Image.open('flame.png').resize((size, size), Image.Resampling.NEAREST),(0, size*3))
    
if os.path.isfile('lava.png') is True:
    new_image.paste(Image.open('lava.png').resize((size, size), Image.Resampling.NEAREST),(size, size*3))
    
if os.path.isfile('note.png') is True:
    new_image.paste(Image.open('note.png').resize((size, size), Image.Resampling.NEAREST),(0, size*4))
    
if os.path.isfile('critical_hit.png') is True:
    new_image.paste(Image.open('critical_hit.png').resize((size, size), Image.Resampling.NEAREST),(size, size*4))

if os.path.isfile('enchanted_hit.png') is True:
    new_image.paste(Image.open('enchanted_hit.png').resize((size, size), Image.Resampling.NEAREST),(size*2, size*4))

if os.path.isfile('heart.png') is True:
    new_image.paste(Image.open('heart.png').resize((size, size), Image.Resampling.NEAREST),(0, size*5))

if os.path.isfile('angry.png') is True:
    new_image.paste(Image.open('angry.png').resize((size, size), Image.Resampling.NEAREST),(size, size*5))

if os.path.isfile('glint.png') is True:
    new_image.paste(Image.open('glint.png').resize((size, size), Image.Resampling.NEAREST),(size*2, size*5))

if os.path.isfile('drip_fall.png') is True:
    new_image.paste(Image.open('drip_fall.png').resize((size, size), Image.Resampling.NEAREST),(0, size*7))
    
if os.path.isfile('drip_hang.png') is True:
    new_image.paste(Image.open('drip_hang.png').resize((size, size), Image.Resampling.NEAREST),(size, size*7))

if os.path.isfile('drip_land.png') is True:
    new_image.paste(Image.open('drip_land.png').resize((size, size), Image.Resampling.NEAREST),(size*2, size*7))

if os.path.isfile('effect_0.png') is True:
    for i in range(0, 8):
        new_image.paste(Image.open('effect_'+str(i)+'.png').resize((size, size), Image.Resampling.NEAREST),(size*i, size*8))

if os.path.isfile('spell_0.png') is True:
    for i in range(0, 8):
        new_image.paste(Image.open('spell_'+str(i)+'.png').resize((size, size), Image.Resampling.NEAREST),(size*i, size*9))

if os.path.isfile('spark_0.png') is True:
    for i in range(0, 8):
        new_image.paste(Image.open('spark_'+str(i)+'.png').resize((size, size), Image.Resampling.NEAREST),(size*i, size*10))

if os.path.isfile('sga_a.png') is True:
    for i in range(0, 15):
        new_image.paste(Image.open('sga_'+ench[i]+'.png').resize((size, size), Image.Resampling.NEAREST),(size*(i+1), size*12))

    for i in range(0, 11):
        new_image.paste(Image.open('sga_'+ench[i+15]+'.png').resize((size, size), Image.Resampling.NEAREST),(size*i, size*13))

new_image.save('particles.png')

#Explosion
if os.path.isfile('explosion_0.png') is True:
    size = Image.open('explosion_0.png').size[0]
    explosion = Image.new(mode = "RGBA", size = (size*4, size*4), color = (255, 255, 255, 0))
    for i in range(0, 4):
        for j in range(0, 4):
            explosion.paste(Image.open('explosion_'+ str(i + j*4) +'.png'),(size*i, size*j))

    explosion.save('explosion.png')


