import argparse
import sys
import json
import os

def loadArgs(path='args.json'):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Construct the full path to args.json
    full_path = os.path.join(script_dir, path)
    
    with open(full_path) as args_file:
        args = json.load(args_file)
    
    # Add positional arguments first
    if 'path_to_rom' in args and 'path_to_rom' not in sys.argv:
        sys.argv.append(args['path_to_rom'])
    
    # Add optional arguments
    for arg in args:
        if arg == 'path_to_rom':
            continue
        name = '--' + arg
        value = args[arg]
        if name not in sys.argv:
            sys.argv.append(name)
            sys.argv.append(value)

    print("Args loaded!")

def main():

    loadArgs()
    parser = argparse.ArgumentParser(description='NES emulator')
    parser.add_argument('path_to_rom', 
                        metavar='R', 
                        type=str,
                        help='Path to NES rom')

    args = parser.parse_args()
    print("Rom path: "+args.path_to_rom)
    
    with open(args.path_to_rom, 'rb') as file:
        lines = file.readlines()

    print(lines)

if __name__ == '__main__':
    main()