from PIL import Image
base = Image.open('zombie_villager.png').convert("RGBA")
base.save('base0.png')
base.paste(Image.open('type/plains.png').convert("RGBA"), (0, 0),mask=Image.open('type/plains.png').convert("RGBA"))
base.save('base.png')

new = ['butcher','farmer','librarian','cleric','toolsmith','nitwit']
old = ['butcher','farmer','librarian','priest','smith','villager']

for i in range(0, len(new)):
    villager = Image.open('base.png').convert("RGBA")
    job = Image.open('profession/' + new[i] + '.png').convert("RGBA")
    villager.paste(job, (0,0), mask=job)
    villager.save(old[i]+".png","PNG")

# ---

pixel = int(base.size[0] / 64)

base = Image.open('base.png').convert("RGBA")

top = base.crop((22*pixel ,20*pixel, 40*pixel, 26*pixel))
top = top.resize((18*pixel, 4*pixel), Image.LANCZOS)
#top.save("top.png", "PNG")

right = base.crop((16*pixel ,26*pixel, 22*pixel, 38*pixel))
right = right.resize((4*pixel, 12*pixel), Image.LANCZOS)
#right.save("right.png", "PNG")

left = base.crop((30*pixel ,26*pixel, 36*pixel, 38*pixel))
left = left.resize((4*pixel, 12*pixel), Image.LANCZOS)
#left.save("left.png", "PNG")

legs = base.crop((0*pixel ,22*pixel, 16*pixel, 38*pixel))
#legs.save("legs.png", "PNG")

front = base.crop((22*pixel ,26*pixel, 30*pixel, 38*pixel))
#front.save("front.png", "PNG")

back = base.crop((36*pixel ,26*pixel, 44*pixel, 38*pixel))
#back.save("back.png", "PNG")

arms = base.crop((44*pixel, 22*pixel, 60*pixel ,38*pixel))
#arms.save("arms.png", "PNG")

head = base.crop((0, 0, 32*pixel ,18*pixel))
#head.save("head.png", "PNG")

background = Image.new(mode = "RGBA", size = (64*pixel, 64*pixel), color = (255, 255, 255, 0))
background.paste(legs, (0, 16*pixel))
background.paste(right, (16*pixel, 20*pixel))

background.paste(front, (20*pixel, 20*pixel))

background.paste(left, (28*pixel, 20*pixel))
background.paste(back, (32*pixel, 20*pixel))

background.paste(arms, (40*pixel, 16*pixel))
background.paste(top, (20*pixel, 16*pixel))
background.paste(head, (0, 32*pixel))
"""
"""
background.save("zombie_villager.png", "PNG")





