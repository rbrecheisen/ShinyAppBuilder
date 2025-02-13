import os
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('app_name', help='Name of the Shiny app')
    parser.add_argument('code_dir', help='Directory containing source code for the Shiny app')
    parser.add_argument('r_dir', help='Directory containing portable R installation')
    parser.add_argument('output_dir', help='Output directory to store Shiny app project')
    args = parser.parse_args()

    app_dir = os.path.join(args.output_dir, args.app_name)

    print('Creating app directory...')
    os.makedirs(app_dir, exist_ok=False)

    print('Copying portable R installation...')
    shutil.copytree(args.r_dir, os.path.join(app_dir, 'R-Portable'))
    
    print('Copying app code')
    shutil.copytree(args.code_dir, app_dir, dirs_exist_ok=True)
    
    shutil.copy('app.bat', app_dir)
    shutil.copy('app.sh', app_dir)
    shutil.copy('app.R', app_dir)
    shutil.copy('run_app.R', app_dir)

    print('Done')


if __name__ == '__main__':
    main()