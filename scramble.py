#!env python
from PIL import Image
seq = '3157629480'
orig = Image.open('%s.png' % seq)
w = orig.size[0]
block_width = w/10
h = orig.size[1]
order = [int(ch) for ch in seq]
print(block_width, h, order)
result = Image.new(orig.mode, orig.size)
for n, i in enumerate(order):
    block = (i*block_width, 0, (i+1)*block_width, h)
    result.paste(orig.crop(block), (n*block_width, 0, (n+1)*block_width, h))

result.save('%s_scrambled_1.png' % seq)
result2 = Image.new(orig.mode, orig.size)
block_height = 23
print(block_height, w, order)
for r in xrange(h/23/10):
    for n, i in enumerate(order):
        block = (0, (r+1)*i*block_height, w, (i*(r+1)+1)*block_height)
        print(block)
        result2.paste(result.crop(block), (0, n*block_height*(r+1), w, (n*(r+1)+1)*block_height))
result2.save('%s_scrambled.png' % seq)
