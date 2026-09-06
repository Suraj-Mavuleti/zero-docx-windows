#!/usr/bin/env python3
import sys, os, argparse

def show_header():
    print("\033[1;34m" + "="*60 + "\033[0m")
    print("\033[1;34m          ZERO-DOCX: TERMINAL DOCUMENT PROCESSOR V3.0\033[0m")
    print("\033[1;34m" + "="*60 + "\033[0m")

def editor_mode(filename):
    print(f"\033[3mEntering editor mode for '{filename}'. Type ':wq' on a new line to save and exit.\033[0m\n")
    lines = []
    while True:
        try:
            line = input("\033[1;32m> \033[0m")
            if line.strip() == ':wq':
                break
            lines.append(line)
        except (KeyboardInterrupt, EOFError):
            break
    
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))
    print(f"\n\033[1;32m[Success]: Saved {len(lines)} lines to {filename}\033[0m")

def read_mode(filename):
    if not os.path.exists(filename):
        print(f"\033[1;31m[Error]: File '{filename}' not found.\033[0m")
        return
    
    with open(filename, 'r') as f:
        content = f.read()
        
    words = len(content.split())
    chars = len(content)
    lines = len(content.split('\n'))
    
    print("\033[1;36m--- DOCUMENT START ---\033[0m")
    print(content)
    print("\033[1;36m--- DOCUMENT END ---\033[0m")
    print(f"\033[1;33m[Stats]: {words} words | {lines} lines | {chars} characters | {chars} bytes\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Zero-Docx Terminal Engine")
    parser.add_argument('file', nargs='?', help="File to edit or read")
    parser.add_argument('-r', '--read', action='store_true', help="Read mode")
    args = parser.parse_args()
    
    show_header()
    
    if not args.file:
        print("\033[1;33mUsage: ./start.sh <filename> [-r]\033[0m")
        print("Example 1: ./start.sh mydoc.txt     (Creates & edits a document)")
        print("Example 2: ./start.sh mydoc.txt -r  (Reads and calculates stats)")
        sys.exit(1)
        
    if args.read:
        read_mode(args.file)
    else:
        editor_mode(args.file)

if __name__ == '__main__':
    main()
