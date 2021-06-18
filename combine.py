import sys, os


#top_folder = sys.argv[1]
output_name = "total_dfasta"

top_folder = sys.argv[1]

parent_folder = os.path.split(os.path.abspath(top_folder))[0]

dest_folder = os.path.join(parent_folder, output_name)

all_subs = []

for item in os.listdir(top_folder):
    if os.path.isdir(os.path.join(top_folder, item)):
        all_subs.append(os.path.join(top_folder, item))


example_dir = ""
if len(all_subs) != 0:
    example_dir = all_subs[0]


import shutil

def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

if len(all_subs) != 0:
    shutil.copytree(all_subs[0], dest_folder, ignore=ig_f)


sub_files = []

for (head, dirs, files) in os.walk(all_subs[0]):
    for file in files:
        rel_dir = os.path.relpath(head, all_subs[0])
        rel_file = os.path.join(rel_dir, file)
        #with_name = current_file_path + "/"+ file


        if rel_file.startswith("./"):
            rel_file = rel_file[2:]
        sub_files.append(rel_file)

import subprocess

for file in sub_files:
    print ("Combining: ", file, "...")
    files = []
    for sub in all_subs:

        files.append (os.path.join(sub, file))

    target_file = os.path.join(dest_folder, file)
    with open(target_file, "w") as outfile:
        subprocess.run(['cat'] + files, stdout=outfile)