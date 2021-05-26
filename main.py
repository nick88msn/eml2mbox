#!/usr/bin/env python3

import os
import sys
import argparse
from pathlib import Path
import mailbox

def parse_args():
    parser = argparse.ArgumentParser(description='Converts single or multiple eml files into an mbox')
    parser.add_argument("input", type=str, help="Eml file or folder to be parsed", default=os.path.join(os.getcwd(),'input'))
    parser.add_argument("output", type=str, help="Destination folder of the final mbox file. If ", default=os.path.join(os.getcwd(),'input'))
    args = parser.parse_args()
    return args

def path_check(path):
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(),path)
    return path

def createMboxFromSingleEml(eml_file, output_path):
    # Here the default output name
    dest_name = 'output.mbox'
    # Create a mbox folder if not present or reference to an existing one if provided
    dest_mbox = mailbox.mbox(os.path.join(output_path,dest_name), create=True)
    dest_mbox.lock()

    with open(eml_file,'rb') as file:
        try:
            dest_mbox.add(file)
        except:
            dest_mbox.close()
            raise
    dest_mbox.close()

def main():
    args = parse_args()
    # Check input file
    eml_path = args.input
    ## Input check: Is the path absolute or relative
    eml_path = path_check(eml_path)

    # Check output
    output_path = args.output
    output_path = path_check(output_path)

    ## Input check: Is the path a directory or a file
    if os.path.isdir(eml_path):
        ### If is a folder launch an iteration and add files to the mbox
        createMboxFromMultipleEmls(eml_path, output_path)
    elif os.path.isfile(eml_path):
        if Path(eml_path).suffix == '.eml':
            ### If is an eml file choose a simpler function
            createMboxFromSingleEml(eml_path, output_path)
    else:
        print('Provide a folder or an eml file.')


if __name__ == '__main__':
    print('''

  ______   __  __   _          _______    ____      __  __   ____     ____   __   __
 |  ____| |  \/  | | |        |__   __|  / __ \    |  \/  | |  _ \   / __ \  \ \ / /
 | |__    | \  / | | |           | |    | |  | |   | \  / | | |_) | | |  | |  \ V / 
 |  __|   | |\/| | | |           | |    | |  | |   | |\/| | |  _ <  | |  | |   > <  
 | |____  | |  | | | |____       | |    | |__| |   | |  | | | |_) | | |__| |  / . \ 
 |______| |_|  |_| |______|      |_|     \____/    |_|  |_| |____/   \____/  /_/ \_\
                                                                                    
                                                                                    
 Convert your eml files into an mbox folder.
 https://github.com/nick88msn/eml2mbox
    ''')

    main()
