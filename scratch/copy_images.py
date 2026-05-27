import os
import shutil

# Target directory in workspace
target_dir = os.path.abspath("assets/images")
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"Created directory: {target_dir}")

# Source file details
brain_dir = r"C:\Users\mark\.gemini\antigravity\brain\415b7b97-d415-43ae-b834-8baa3ee87328"
src_files = {
    "descent_of_orpheus_1779734796606.png": "descent_of_orpheus.png",
    "the_resurrection_1779734811828.png": "the_resurrection.png"
}

for src_name, dest_name in src_files.items():
    src_path = os.path.join(brain_dir, src_name)
    dest_path = os.path.join(target_dir, dest_name)
    
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied {src_name} to {dest_path}")
    else:
        print(f"Source file {src_path} not found!")
