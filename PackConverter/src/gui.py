from PIL import Image
import os
#Read Images

size = 18 #temp
if os.path.isfile('speed.png') is True:
    image = Image.open('speed.png')
    size = int(image.size[0])

multiplier = size/18


image = Image.open('inventory.png')
size2 = int(image.size[0])
multiplier2 = size2/256

new_image = (Image.open('inventory.png').resize( (int(size2*multiplier), int(size2*multiplier)) , Image.Resampling.NEAREST)).convert('RGBA')

ench = 'abcdefghijklmnopqrstuvwxyz'

row1 = ['speed', 'slowness', 'haste', 'mining_fatigue', 'strength', 'weakness', 'poison', 'regeneration']
row2 = ['invisibility', 'hunger', 'jump_boost', 'nausea', 'night_vision', 'blindness', 'resistance', 'fire_resistance']
row3 = ['water_breathing', 'wither', 'absorption']

k = 0
base = (Image.open('mob_effect/effects_base.png').resize((int(size2*multiplier), int(size2*multiplier)), Image.Resampling.NEAREST)).convert('RGBA')
new_image.paste(base,(k, int(198*multiplier2*multiplier)), base)


for i in row1:
    if os.path.isfile('mob_effect/'+i+'.png') is True:
        new_image.paste((Image.open('mob_effect/'+i+'.png').resize((int(size*multiplier2), int(size*multiplier2)), Image.Resampling.NEAREST)).convert('RGBA'),(k, int(198*multiplier2*multiplier)))
    k = k + int(size*multiplier2)

k = 0
for i in row2:
    if os.path.isfile('mob_effect/'+i+'.png') is True:
        new_image.paste((Image.open('mob_effect/'+i+'.png').resize((int(size*multiplier2), int(size*multiplier2)), Image.Resampling.NEAREST)).convert('RGBA'),(k, int(size*multiplier2 + 198*multiplier2*multiplier)))
    k = k + int(size*multiplier2)

k = 0
for i in row3:
    if os.path.isfile('mob_effect/'+i+'.png') is True:
        new_image.paste((Image.open('mob_effect/'+i+'.png').resize((int(size*multiplier2), int(size*multiplier2)), Image.Resampling.NEAREST)).convert('RGBA'),(k, int(size*2*multiplier2 + 198*multiplier2*multiplier)))
    k = k + int(size*multiplier2)

new_image.save('inventory.png')
#new_image.show()
