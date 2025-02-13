import os
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('code_dir', help='Directory containing source code for Shiny app')
    parser.add_argument('output_dir', help='Output directory where to store app')
    parser.add_argument('r_dir', help='Directory containing (portable) R installation')
    args = parser.parse_args()
    
    print('Copying portable R environment into app directory...')
    shutil.copytree(args.r_dir, os.path.join(args.output_dir, os.path.split(args.r_dir)[1]))
    shutil.copy()

    print('Done')


if __name__ == '__main__':
    main()