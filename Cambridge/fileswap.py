import os
import re

# 현재 디렉토리에서 작업 (필요시 경로 수정)
target_dir = "."

# split_part 파일 탐색
for filename in os.listdir(target_dir):
    if filename.startswith("split_part_") and filename.endswith(".md"):
        match = re.search(r"split_part_(\d+)\.md", filename)
        if match:
            src_num = int(match.group(1))
            target_num = src_num - 3  # 번호 - 3
            target_prefix = f"{target_num:02d}-"

            # 대상 파일 탐색
            for tf in os.listdir(target_dir):
                if tf.startswith(target_prefix) and tf.endswith(".md"):
                    print(f"Inserting '{filename}' into '{tf}'")

                    with open(os.path.join(target_dir, filename), "r", encoding="utf-8") as f_src:
                        content_to_insert = f_src.read()

                    with open(os.path.join(target_dir, tf), "a", encoding="utf-8") as f_target:
                        f_target.write("\n\n---\n\n")
                        f_target.write(content_to_insert)