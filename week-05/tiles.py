length = 12
width = 6

tiles_needed = length * width
extra_tiles = tiles_needed * 1.10

boxes_needed = round(extra_tiles / 6)

print("need to buy" , boxes_needed, "boxes of tiles")
