import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cấu hình nhiều topic ở đây
TOPICS = [
    {
        "name": "Array",
        "doc": os.path.join(BASE_DIR, "Docs", "Array.md"),
        "leet_path": os.path.join(BASE_DIR, "Solutions", "LeetCode", "Arrays"),
        "gfg_path": os.path.join(BASE_DIR, "Solutions", "GeeksforGeeks", "Arrays"),
        "target": 200
    },
    {
        "name": "String",
        "doc": os.path.join(BASE_DIR, "Docs", "String.md"),
        "leet_path": os.path.join(BASE_DIR, "Solutions", "LeetCode", "Strings"),
        "gfg_path": os.path.join(BASE_DIR, "Solutions", "GeeksforGeeks", "Strings"),
        "target": 150
    },
]

PROBLEM_REGEX = re.compile(r"^(\d{3,4})_(.+)$")

def normalize_name(name):
    return " ".join(word.capitalize() for word in re.split("[-_]", name))

def progress_bar(done, total, length=20):
    percent = int((done / total) * 100) if total else 0
    filled = int(length * percent / 100)
    bar = "█" * filled + "-" * (length - filled)
    return f"**Progress:** {done} / {total} ({percent}%)\n\n`[{bar}]`"

def collect_problems(base_path, site):
    problems = {}  # Sử dụng dict để tránh trùng lặp
    if not os.path.exists(base_path):
        return problems
    
    for folder in os.listdir(base_path):
        path = os.path.join(base_path, folder)
        if os.path.isdir(path):
            match = PROBLEM_REGEX.match(folder)
            if match:
                pid, raw_name = match.groups()
                pname = normalize_name(raw_name)
            else:
                pid, pname = "----", normalize_name(folder)
                raw_name = folder
            
            if site == "LeetCode":
                link = f"https://leetcode.com/problems/{raw_name.replace('_','-')}/"
            else:
                link = f"https://www.geeksforgeeks.org/{raw_name.replace('_','-')}/"
            
            # Sử dụng ID làm key để tránh trùng lặp
            problems[pid] = {
                "id": pid,
                "name": pname,
                "link": link,
                "status": "✅",
                "note": ""
            }
    
    # Trả về danh sách đã sắp xếp
    return sorted(problems.values(), key=lambda x: (x["id"], x["name"]))

def parse_table_block(content, title):
    pat = re.compile(rf"(### {re.escape(title)}\s*\n.*?)(?=\n### |\Z)", re.DOTALL)
    m = pat.search(content)
    if not m:
        return "", {}, set()
    
    table_block = m.group(1)
    lines = table_block.splitlines()
    header_idx = [i for i, line in enumerate(lines) if line.strip().startswith("| ID")]
    
    existing_problems = {}  # Sử dụng dict với ID làm key
    old_ids = set()
    
    if header_idx:
        start = header_idx[0] + 2
        for line in lines[start:]:
            line = line.strip()
            if line.startswith("|") and not line.startswith("| ----") and line != "":
                cells = [c.strip() for c in line.split("|")]
                if len(cells) >= 6 and cells[1] != "":  # Đảm bảo có đủ cells
                    id_ = cells[1]
                    if id_ not in old_ids:  # Chỉ thêm nếu chưa có
                        existing_problems[id_] = line
                        old_ids.add(id_)
    
    return table_block, existing_problems, old_ids

def update_table_block(table_block, existing_problems, old_ids, new_problems, title, target):
    added = 0
    
    # Merge existing và new problems
    all_problems = dict(existing_problems)  # Copy existing
    
    for p in new_problems:
        if p["id"] not in old_ids:
            all_problems[p["id"]] = f"| {p['id']} | {p['name']} | [Link]({p['link']}) | {p['status']} | {p['note']} |"
            old_ids.add(p["id"])
            added += 1
    
    solved = len(old_ids)
    progress = progress_bar(solved, target)
    
    # Sắp xếp các problems theo ID
    sorted_rows = []
    for pid in sorted(all_problems.keys(), key=lambda x: (x.zfill(4), x)):  # Sắp xếp số đúng cách
        sorted_rows.append(all_problems[pid] + "\n")
    
    # Tạo block mới
    new_block = (
        f"### {title}\n\n"
        + progress
        + "\n\n"
        + "| ID | Problem | Link | Status | Note |\n"
        + "| ---- | ------- | ---- | ------ | ---- |\n"
        + "".join(sorted_rows)
        + "\n"
    )
    
    return new_block, added

def update_doc():
    for topic in TOPICS:
        print(f"🔄 Đang xử lý topic: {topic['name']}")
        
        # Kiểm tra file tồn tại
        if not os.path.exists(topic["doc"]):
            print(f"⚠️  File {topic['doc']} không tồn tại!")
            continue
        
        with open(topic["doc"], "r", encoding="utf-8") as f:
            content = f.read()
        
        # LeetCode
        leet_table_block, leet_existing, leet_ids = parse_table_block(content, "📘 LeetCode Problems")
        leet_problems = collect_problems(topic["leet_path"], "LeetCode")
        leet_new_block, leet_added = update_table_block(
            leet_table_block, leet_existing, leet_ids, leet_problems, "📘 LeetCode Problems", topic["target"]
        )
        
        # GFG
        gfg_table_block, gfg_existing, gfg_ids = parse_table_block(content, "🟢 GeeksforGeeks Problems")
        gfg_problems = collect_problems(topic["gfg_path"], "GeeksforGeeks")
        gfg_new_block, gfg_added = update_table_block(
            gfg_table_block, gfg_existing, gfg_ids, gfg_problems, "🟢 GeeksforGeeks Problems", topic["target"]
        )
        
        # Thay thế block cũ bằng block mới
        if "📘 LeetCode Problems" in content:
            content = re.sub(
                r"(### 📘 LeetCode Problems\s*\n.*?)(?=\n### |\Z)",
                leet_new_block.rstrip() + "\n",
                content,
                flags=re.DOTALL,
            )
        else:
            content += "\n" + leet_new_block
        
        if "🟢 GeeksforGeeks Problems" in content:
            content = re.sub(
                r"(### 🟢 GeeksforGeeks Problems\s*\n.*?)(?=\n### |\Z)",
                gfg_new_block.rstrip() + "\n",
                content,
                flags=re.DOTALL,
            )
        else:
            content += "\n" + gfg_new_block
        
        # Ghi file
        try:
            with open(topic["doc"], "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ [{topic['name']}] Cập nhật thành công! LeetCode: +{leet_added}, GFG: +{gfg_added} problem mới.")
        except Exception as e:
            print(f"❌ Lỗi khi ghi file {topic['doc']}: {e}")

if __name__ == "__main__":
    update_doc()