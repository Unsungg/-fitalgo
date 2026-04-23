import shutil

img_192 = r"C:\Users\iremo\.gemini\antigravity\brain\2bb5912f-c8bb-438c-b83d-dfb40a928e84\purple_dumbbell_192_1776959889838.png"
img_512 = r"C:\Users\iremo\.gemini\antigravity\brain\2bb5912f-c8bb-438c-b83d-dfb40a928e84\purple_dumbbell_512_1776959905404.png"

dest_192 = r"c:\Users\iremo\fitalgo\static\icon-192.png"
dest_512 = r"c:\Users\iremo\fitalgo\static\icon-512.png"

shutil.copyfile(img_192, dest_192)
shutil.copyfile(img_512, dest_512)
print("New icons copied successfully!")
