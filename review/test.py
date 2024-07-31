import json
with open ("forget.json", "r", encoding="UTF-8") as f:
    forget = json.load(f)
print(forget)