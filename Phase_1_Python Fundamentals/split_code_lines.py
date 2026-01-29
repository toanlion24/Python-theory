import json
import re

# Read the notebook
with open('Python_Basics_Quiz_Advanced_100_Questions.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

def split_code_line(code_lines):
    """Split single line code with semicolons into multiple lines"""
    if not code_lines:
        return code_lines
    
    # Join all lines first
    full_code = ''.join(code_lines)
    
    # Handle special cases that need multiple lines (functions, try-except, etc.)
    if 'def ' in full_code or 'try:' in full_code or 'for ' in full_code or 'if ' in full_code or 'else:' in full_code:
        # Already multi-line, just ensure proper formatting
        lines = full_code.strip().split('\n')
        return [line + '\n' for line in lines[:-1]] + [lines[-1]] if lines else []
    
    # Split by semicolon but preserve string literals
    parts = []
    current_part = []
    in_string = False
    quote_char = None
    paren_count = 0
    bracket_count = 0
    brace_count = 0
    
    i = 0
    while i < len(full_code):
        char = full_code[i]
        
        if not in_string:
            if char in ['"', "'"]:
                in_string = True
                quote_char = char
                current_part.append(char)
            elif char == ';':
                if paren_count == 0 and bracket_count == 0 and brace_count == 0:
                    part = ''.join(current_part).strip()
                    if part:
                        parts.append(part)
                    current_part = []
                else:
                    current_part.append(char)
            elif char == '(':
                paren_count += 1
                current_part.append(char)
            elif char == ')':
                paren_count -= 1
                current_part.append(char)
            elif char == '[':
                bracket_count += 1
                current_part.append(char)
            elif char == ']':
                bracket_count -= 1
                current_part.append(char)
            elif char == '{':
                brace_count += 1
                current_part.append(char)
            elif char == '}':
                brace_count -= 1
                current_part.append(char)
            else:
                current_part.append(char)
        else:
            current_part.append(char)
            if char == quote_char and full_code[i-1] != '\\':
                in_string = False
                quote_char = None
        
        i += 1
    
    # Add remaining part
    if current_part:
        part = ''.join(current_part).strip()
        if part:
            parts.append(part)
    
    # Convert to list format for notebook
    if parts:
        return [part + '\n' for part in parts[:-1]] + [parts[-1]]
    return code_lines

# Process all code cells
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        if 'source' in cell and cell['source']:
            # Check if it's a single line with semicolons
            source_str = ''.join(cell['source'])
            
            # Skip if already multi-line or is a function/control structure
            if ';' in source_str and ('def ' not in source_str and 'try:' not in source_str and 
                                       'for ' not in source_str and 'if ' not in source_str and
                                       'else:' not in source_str and 'import ' not in source_str):
                # Split into multiple lines
                new_source = split_code_line(cell['source'])
                if new_source:
                    cell['source'] = new_source

# Write back
with open('Python_Basics_Quiz_Advanced_100_Questions.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Split single-line code into multiple lines!")
