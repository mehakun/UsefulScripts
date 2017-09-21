#!/usr/bin/env python3

import os, shutil, sys

def make_quest_src_dict(quest_filename, src_dir, prefix):
    with open(quest_filename, 'r') as q_file:
        result = {line.rstrip('\n') : [] for line in q_file}
        
        with os.scandir(src_dir) as src:
            for entry in src:
                if entry.name.startswith(prefix) and entry.is_file():
                    for quest, val in result.items():
                        if entry.name.startswith(quest[:2], len(prefix)):
                            val.append(entry.path)
                
        return result
            
def make_dirs_and_move(files_dict, dest):
    for quest, files_list in files_dict.items():
        quest_dir = dest + '/' + quest
        
        if not os.path.exists(quest_dir):
            os.mkdir(quest_dir)

        for moving_file in files_list:
            shutil.move(moving_file, quest_dir)

def helper():
    print("Usage:")
    print("move_to_dirs <file_with_questions> <prefix_of_files_to_move> <destination_dir> <source_dir>")
    print("To show help: move_to_dirs -h")
            
if __name__ == "__main__":
    quest_filename = sys.argv[1]

    if quest_filename == "-h" or not os.path.isfile(quest_filename):
        helper()
        quit()
    
    prefix_of_files = sys.argv[2]
    dest_dir = sys.argv[3]
    dir_with_files = sys.argv[4]

    if not os.path.isdir(dest_dir) or not os.path.isdir(dir_with_files):
        helper()
        quit()

    qst_src_dict = make_quest_src_dict(quest_filename, dir_with_files, prefix_of_files)
    make_dirs_and_move(qst_src_dict, os.path.abspath(dest_dir))

