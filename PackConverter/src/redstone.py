from PIL import Image
import os

if os.path.isfile("redstone_dust_line0.png") is True:  # redstone
    os.rename("redstone_dust_line0.png" , "redstone_dust_line.png")

if os.path.isfile("redstone_dust_line0.png.mcmeta") is True: 
    os.rename("redstone_dust_line0.png.mcmeta" , "redstone_dust_line.png.mcmeta")

line0 = (Image.open("redstone_dust_line.png")).rotate(90).convert("RGBA")
line1 = Image.open("redstone_dust_line1.png").convert("RGBA")
dot = Image.open("redstone_dust_dot.png").convert("RGBA")
size = dot.size[0]

cross = Image.new(mode = "RGBA", size = (size, size), color = (255, 255, 255, 0))
cross.paste(line0, (0, 0), mask=line0)
cross.paste(line1, (0, 0), mask=line1)
cross.paste(dot, (0, 0), mask=dot)

cross.save("redstone_dust_cross.png","PNG")
line0.save("redstone_dust_line.png","PNG")


"""
for banner in banners:
    foreground = Image.open(banner)
    background.paste(foreground, (0, 0),mask=foreground)
    background.save(banner,"PNG")
    background = Image.new(mode = "RGBA", size = (dim, dim), color = (0, 0, 0, 255))

"""
