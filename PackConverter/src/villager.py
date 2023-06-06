from PIL import Image
base = Image.open('villager.png').convert("RGBA")
base.save('base0.png')
base.paste(Image.open('type/plains.png').convert("RGBA"), (0, 0),mask=Image.open('type/plains.png').convert("RGBA"))
base.save('base.png')

new = ['butcher','farmer','librarian','cleric','toolsmith','nitwit']
old = ['butcher','farmer','librarian','priest','smith','villager']

for i in range(0, len(new)):
    villager = Image.open('base.png')
    job = Image.open('profession/' + new[i] + '.png').convert("RGBA")
    villager.paste(job, (0,0), mask=job)
    villager.save(old[i]+".png","PNG")
