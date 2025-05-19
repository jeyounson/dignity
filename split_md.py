# split_md.py
import os

# 설정
input_file = "PhilosophicalFoundationsofHumanRights/z_all-chpters_PhilosophicalFoundationsofHumanRights.md"
split_marker = "<!-- SPLIT HERE -->"
output_prefix = "chapter_"

# 읽기
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# 분할
parts = content.split(split_marker)

# 저장
for idx, part in enumerate(parts, start=1):
    filename = f"{output_prefix}{idx}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(part.strip())
    print(f"Saved: {filename}")