import re
import pathlib

skill_file = pathlib.Path('skills/02-initiating/SKL-02-01-project-charter.md')
content = skill_file.read_text(encoding='utf-8')

# Parse frontmatter and body
match = re.match(r'^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$', content)
body = match.group(2)

# Find where Instructions starts
instr_idx = body.find('## Instructions')
if instr_idx != -1:
    # Show what's after Instructions
    after_instr = body[instr_idx:instr_idx+2000]
    print("First 2000 chars after '## Instructions':")
    print(repr(after_instr[:800]))
    print("\n---\n")
    
    # Try different regex patterns for finding instructions content
    patterns = [
        r'## Instructions\r?\n\r?\n([\s\S]*?)(?=\n## |\n\r?\n---)',  # Up to next ## or ---
        r'## Instructions\r?\n\r?\n([\s\S]*)',  # Everything after
        r'## Instructions([\s\S]*?)(?=\n## [A-Z])',  # Up to next section header
    ]
    
    for i, pattern in enumerate(patterns, 1):
        match = re.search(pattern, body)
        if match:
            content = match.group(1).strip()
            step_count = len(re.findall(r'### Step \d+', content))
            print(f"Pattern {i} matched, length={len(content)}, steps found={step_count}")
            if step_count > 0:
                print(f"  First 200 chars: {content[:200]}")
        else:
            print(f"Pattern {i} did not match")
