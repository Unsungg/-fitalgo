import json

with open(r'C:\Users\iremo\.gemini\antigravity\brain\2bb5912f-c8bb-438c-b83d-dfb40a928e84\.system_generated\steps\48\content.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    json_str = lines[4] # Line 5 has the JSON
    data = json.loads(json_str)

for item in data.get('tree', []):
    path = item.get('path', '')
    if 'rope' in path.lower() or 'jump' in path.lower() or 'plank' in path.lower():
        print(path)
