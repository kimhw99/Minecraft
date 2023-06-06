from PIL import Image

banners = ['base.png', 'border.png', 'bricks.png', 'circle.png', 'creeper.png', 'cross.png', 'curly_border.png', 'diagonal_left.png', 'diagonal_right.png', 'diagonal_up_left.png', 'diagonal_up_right.png', 'flower.png', 'globe.png', 'gradient.png', 'gradient_up.png', 'half_horizontal.png', 'half_horizontal_bottom.png', 'half_vertical.png', 'half_vertical_right.png', 'mojang.png', 'rhombus.png', 'skull.png', 'small_stripes.png', 'square_bottom_left.png', 'square_bottom_right.png', 'square_top_left.png', 'square_top_right.png', 'straight_cross.png', 'stripe_bottom.png', 'stripe_center.png', 'stripe_downleft.png', 'stripe_downright.png', 'stripe_left.png', 'stripe_middle.png', 'stripe_right.png', 'stripe_top.png', 'triangles_bottom.png', 'triangles_top.png', 'triangle_bottom.png', 'triangle_top.png']

dim = (Image.open("small_stripes.png").size)[0]
background = Image.new(mode = "RGBA", size = (dim, dim), color = (0, 0, 0, 255))

for banner in banners:
    foreground = Image.open(banner)
    background.paste(foreground, (0, 0),mask=foreground)
    background.save(banner,"PNG")
    background = Image.new(mode = "RGBA", size = (dim, dim), color = (0, 0, 0, 255))
