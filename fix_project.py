import os
import re

workout_path = r'c:\Users\iremo\fitalgo\templates\workout.html'
with open(workout_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Translate texts
content = content.replace('Gorsel+Bulunamadi', 'Image+Not+Found')
content = content.replace('Egzersiz Animasyonu', 'Exercise Animation')
content = content.replace('Yükleniyor...', 'Loading...')
content = content.replace('Hareketin doğru formu için animasyonu inceleyin.', 'Observe the animation for the correct form.')
content = content.replace('Tıkla ve animasyonu gör', 'Click to see animation')

# Remove data-tr completely
content = re.sub(r'\s*data-tr="[^"]*"', '', content)

# 2. Fix the missing images in the map
# Set 'HIIT Treadmill': '' and 'Jump Rope': ''
content = content.replace('"Walking"', '""')
content = content.replace('"Jump_Rope"', '""')

with open(workout_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Process other HTML files to remove data-tr
templates_dir = r'c:\Users\iremo\fitalgo\templates'
for fname in os.listdir(templates_dir):
    if fname.endswith('.html') and fname != 'workout.html':
        fpath = os.path.join(templates_dir, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        c_new = re.sub(r'\s*data-tr="[^"]*"', '', c)
        if c_new != c:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c_new)

# Empty out lang.js so it does not add any Turkish language buttons or replace text
lang_js_path = r'c:\Users\iremo\fitalgo\static\lang.js'
if os.path.exists(lang_js_path):
    with open(lang_js_path, 'w', encoding='utf-8') as f:
        f.write('')

print("Project fixed successfully!")
