# -*- coding: utf-8 -*-
from pillow_heif import register_heif_opener
from PIL import Image
import sys

register_heif_opener()

for i in sys.argv[1:]:
    print(i)
    image = Image.open(i)
    image.save(i + '.png', 'PNG')
