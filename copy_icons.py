import shutil

img_192 = r"C:\Users\iremo\.gemini\antigravity\brain\2bb5912f-c8bb-438c-b83d-dfb40a928e84\fitalgo_icon_192_1776958430513.png"
img_512 = r"C:\Users\iremo\.gemini\antigravity\brain\2bb5912f-c8bb-438c-b83d-dfb40a928e84\fitalgo_icon_512_1776958443084.png"

dest_192 = r"c:\Users\iremo\fitalgo\static\icon-192.png"
dest_512 = r"c:\Users\iremo\fitalgo\static\icon-512.png"

shutil.copyfile(img_192, dest_192)
shutil.copyfile(img_512, dest_512)
