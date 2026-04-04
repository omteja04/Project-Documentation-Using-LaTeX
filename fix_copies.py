import os
import re

copies_dir = "Copies"
students = ["Omteja", "Deepika", "Sai_Gayatri_Vishwesh", "Ankit_Roy_Chowdhury"]

for student in students:
    target_dir = os.path.join(copies_dir, f"Doc_{student}")
    
    # 1. Fix title.tex tabular space
    title_path = os.path.join(target_dir, "initial_pages", "title.tex")
    if os.path.exists(title_path):
        with open(title_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r"\\begin\{tabular\}\{p\{9cm\} r\}\s*\\textbf\{([^}]+)\}\s*&\s*\\textbf\{\(([^)]+)\)\}\s*\\\\.*?\\end\{tabular\}"
        # We replace it so the name and roll number are just text next to each other
        replacement = r"\\textbf{\1 (\2)}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(title_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    # 2. Fix abstract.tex "Batch Members"
    abstract_path = os.path.join(target_dir, "initial_pages", "abstract.tex")
    if os.path.exists(abstract_path):
        with open(abstract_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("Batch Members:", "Student:")
        
        with open(abstract_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Fixes applied successfully to all 4 copies!")
