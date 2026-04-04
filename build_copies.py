import os
import shutil
import re

students = [
    {"id": "Omteja", "full_name": "YALLAPRAGADA OMTEJA", "roll": "22P31A0539"},
    {"id": "Deepika", "full_name": "KARRI DEEPIKA", "roll": "22P31A0517"},
    {"id": "Sai_Gayatri_Vishwesh", "full_name": "DANGETI SAI GAYATRI VISHWESH", "roll": "22P31A0508"},
    {"id": "Ankit_Roy_Chowdhury", "full_name": "ANKIT ROY CHOWDHURY", "roll": "22P31A0504"}
]

src_dir = "."
copies_dir = "Copies"

if not os.path.exists(copies_dir):
    os.makedirs(copies_dir)

def transform_pronouns(text):
    # Fix "We are" -> "I am" before doing generic We -> I
    text = re.sub(r'\bWe are\b', 'I am', text)
    text = re.sub(r'\bwe are\b', 'I am', text)
    text = re.sub(r'\bWe were\b', 'I was', text)
    text = re.sub(r'\bwe were\b', 'I was', text)
    
    # Also "We have" -> "I have" is fine "we" -> "I" covers it.
    
    # Generic replacements
    text = re.sub(r'\bWe\b', 'I', text)
    text = re.sub(r'\bwe\b', 'I', text)
    text = re.sub(r'\bOur\b', 'My', text)
    text = re.sub(r'\bour\b', 'my', text)
    text = re.sub(r'\bUs\b', 'Me', text)
    text = re.sub(r'\bus\b', 'me', text)
    
    # Adjust for grammar like "PROJECT ASSOCIATES" -> "PROJECT ASSOCIATE"
    text = text.replace("PROJECT ASSOCIATES", "PROJECT ASSOCIATE")
    
    # For verbs ending in 's', e.g., "we show" -> "I show" (doesn't need 's'). "we propose" -> "I propose". So no major verb change needed for "I" except "to be".
    return text

def transform_authors_block(text, student):
    # Title Page Replace
    title_pattern = r"\\textbf\{YALLAPRAGADA OMTEJA\}.*?\\end\{tabular\}"
    title_rep = f"\\textbf{{{student['full_name']}}} & \\textbf{{({student['roll']})}} \\\\\n\\end{{tabular}}"
    text = re.sub(title_pattern, lambda m: title_rep, text, flags=re.DOTALL)
    
    # Certificate Page Replace
    cert_pattern = r"\\textbf\{YALLAPRAGADA OMTEJA.*?2025--2026\."
    cert_rep = f"\\textbf{{{student['full_name']} ({student['roll']})}}\n in partial fulfillment of the requirements for the award of the degree of \n\\textbf{{Bachelor of Technology in Computer Science and Engineering}} \nfrom Aditya College of Engineering and Technology, Surampalem, during the academic year 2025--2026."
    text = re.sub(cert_pattern, lambda m: cert_rep, text, flags=re.DOTALL)
    
    # Declaration / Acknowledgement Replace
    assoc_pattern = r"YALLAPRAGADA OMTEJA \(22P31A0539\)\\\\.*?ANKIT ROY CHOWDHURY \(22P31A0504\)"
    assoc_rep = f"{student['full_name']} ({student['roll']})"
    text = re.sub(assoc_pattern, lambda m: assoc_rep, text, flags=re.DOTALL)

    # Abstract replace
    abstract_pattern = r"YALLAPRAGADA OMTEJA \(22P31A0539\).*?ANKIT ROY CHOWDHURY \(22P31A0504\)"
    text = re.sub(abstract_pattern, lambda m: assoc_rep, text, flags=re.DOTALL)

    return text

for student in students:
    target_dir = os.path.join(copies_dir, f"Doc_{student['id']}")
    print(f"Creating {target_dir}...")
    
    def ignore_patterns(dir_path, filenames):
        ignore_list = []
        if os.path.abspath(dir_path) == os.path.abspath(src_dir):
            ignore_list.extend(['Copies', '.git', '.antigravityignore', 'build_copies.py', 'paper'])
        return ignore_list
        
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    
    shutil.copytree(src_dir, target_dir, ignore=ignore_patterns)
    
    # Process tex files
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            if name.endswith('.tex'):
                file_path = os.path.join(root, name)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = transform_pronouns(content)
                content = transform_authors_block(content, student)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    print(f"Finished {student['id']}")

print("All copies created successfully!")
