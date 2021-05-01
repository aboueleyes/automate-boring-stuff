#!/usr/bin/env python3
import os
import qrcode 

img = qrcode.make("https://www.aboueleyes.me")
img.save("blog.png",'PNG')
os.system('feh blog.png')