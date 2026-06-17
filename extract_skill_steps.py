import json
import pathlib
import re

root = pathlib.Path('E:/For laerned/PMOSkills')
skills_dir = root / 'skills'
store_path = root / 'sdk/npm/src/db/store.json'

# Load current store
store = json.loads(store_path.read_text(encoding='utf-8'))

def extract_steps(body):
    """Extract steps from Instructions section"""
    steps = []
    # Use correct lookahead pattern to capture all instructions
    instructions_match = re.search(r'## Instructions\r?\n\r?\n([\s\S]*?)(?=\n## |\n\r?\n---)', body)
    if instructions_match:
        instructions_body = instructions_match.group(1)
        # Find all "### Step N —" patterns and extract the title
        step_pattern = r'### Step \d+\s*[—–\-]\s*([^\n]+)'
        step_matches = re.findall(step_pattern, instructions_body)
        for step_title in step_matches:
            if step_title.strip():
                steps.append(step_title.strip())
    return steps

def extract_inputs_outputs(body):
    """Extract inputs and outputs from tables"""
    inputs = []
    outputs = []
    
    # Extract Inputs from the Inputs Required section
    inputs_match = re.search(r'## Inputs Required\r?\n\r?\n\|([\s\S]*?)(?=\n## |\n\r?\n---|$)', body)
    if inputs_match:
        rows = inputs_match.group(1).split('\n')[2:]
        for row in rows:
            cols = [s.strip() for s in row.split('|')]
            if len(cols) > 2 and cols[1]:
                inputs.append(cols[1])

    # Extract Outputs from the explicit Outputs section
    outputs_match = re.search(r'## Outputs\r?\n\r?\n([\s\S]*?)(?=\n## |\n\r?\n---|$)', body)
    if outputs_match:
        outputs_section = outputs_match.group(1).strip()
        if '\n|' in outputs_section or outputs_section.startswith('|'):
            # Parse markdown table
            rows = outputs_section.split('\n')[2:]
            for row in rows:
                cols = [s.strip() for s in row.split('|')]
                if len(cols) > 1 and cols[0] and cols[0] != '---':
                    outputs.append(cols[0])
        else:
            # Parse bullet list if there is no table
            for line in outputs_section.split('\n'):
                trimmed = line.strip()
                if trimmed.startswith('-') or trimmed.startswith('*'):
                    output = trimmed[1:].strip()
                    output = re.sub(r'\*\*(.*?)\*\*', r'\1', output)
                    if output:
                        outputs.append(output)

    return inputs, outputs

# Process each skill file
skill_files = list(skills_dir.rglob('*.md'))
print(f'Found {len(skill_files)} skill files')

updated_count = 0
for skill_file in skill_files:
    content = skill_file.read_text(encoding='utf-8')
    
    # Parse frontmatter and body
    match = re.match(r'^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$', content)
    if not match:
        continue
    
    metadata_str = match.group(1)
    body = match.group(2)
    
    # Extract skill_id from metadata
    skill_id_match = re.search(r'skill_id:\s*([^\n]+)', metadata_str)
    if not skill_id_match:
        continue
    
    skill_id = skill_id_match.group(1).strip()
    
    # Skip if skill not in store
    if skill_id not in store['skills']:
        continue
    
    # Extract steps, inputs, outputs
    steps = extract_steps(body)
    inputs, outputs = extract_inputs_outputs(body)
    
    # Update store
    if steps:
        store['skills'][skill_id]['steps'] = steps
        updated_count += 1
    
    if inputs:
        store['skills'][skill_id]['inputs'] = inputs
    
    if outputs:
        store['skills'][skill_id]['outputs'] = outputs
    
    # Ensure content is set
    if 'content' not in store['skills'][skill_id]:
        store['skills'][skill_id]['content'] = body.strip()

# Save updated store
store_path.write_text(json.dumps(store, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Updated {updated_count} skills with extracted steps')
print(f'Saved to {store_path}')

# Show sample
if 'SKL-02-01' in store['skills']:
    print(f"\nSample SKL-02-01:")
    skill = store['skills']['SKL-02-01']
    print(f"  Steps: {len(skill.get('steps', []))} steps")
    if skill.get('steps'):
        for i, step in enumerate(skill['steps'][:3], 1):
            print(f"    {i}. {step}")
    print(f"  Inputs: {len(skill.get('inputs', []))} inputs")
    print(f"  Outputs: {len(skill.get('outputs', []))} outputs")
