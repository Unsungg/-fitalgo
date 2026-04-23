import shutil

img_192 = r"c:\Users\iremo\fitalgo\static\icon-192.png"
img_512 = r"c:\Users\iremo\fitalgo\static\icon-512.png"

dest_192 = r"c:\Users\iremo\fitalgo\static\icon-192-v2.png"
dest_512 = r"c:\Users\iremo\fitalgo\static\icon-512-v2.png"

# Since copy_new_icons.py was already run, icon-192.png is the purple dumbbell.
# Let's just duplicate it with a new name.
shutil.copyfile(img_192, dest_192)
shutil.copyfile(img_512, dest_512)
print("v2 icons created to bypass cache.")
