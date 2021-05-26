#!/usr/bin/env python3

import os
import sys
import argparse
import mailbox



def parse_args():
    parser = argparse.ArgumentParser(description='Converts single or multiple eml files into an mbox')
    parser.add_argument("input_file", type=str, help="Eml file or folder to be parsed", default=os.path.join(os.getcwd(),'input'))
    parser.add_argument("output_file", type=str, help="Destination folder and name of the final mbox file. If ", default=os.path.join(os.getcwd(),'input'))
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    print('''

  ______   __  __   _          _______    ____      __  __   ____     ____   __   __
 |  ____| |  \/  | | |        |__   __|  / __ \    |  \/  | |  _ \   / __ \  \ \ / /
 | |__    | \  / | | |           | |    | |  | |   | \  / | | |_) | | |  | |  \ V / 
 |  __|   | |\/| | | |           | |    | |  | |   | |\/| | |  _ <  | |  | |   > <  
 | |____  | |  | | | |____       | |    | |__| |   | |  | | | |_) | | |__| |  / . \ 
 |______| |_|  |_| |______|      |_|     \____/    |_|  |_| |____/   \____/  /_/ \_\
                                                                                    
                                                                                    
    ''')

