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

    print('Checking code for mandatory files...')
    files = os.listdir(args.code_dir)
    assert 'app.R' in files, 'Missing "app.R" file that sources "server.R" and runs Shiny app'
    assert 'ui.R' in files, 'Missing "ui.R" file that contains Shiny app UI'
    assert 'server.R' in files, 'Missing "server.R" file with server-side functionality of Shiny app'
    assert 'dependencies.R' in files, 'Missing "dependencies.R" file'

    print('Creating app directory...')
    os.makedirs(app_dir, exist_ok=False)

    print('Copying portable R installation...')
    shutil.copytree(args.r_dir, os.path.join(app_dir, 'R-Portable'))
    
    print('Copying app code')
    shutil.copytree(args.code_dir, app_dir, dirs_exist_ok=True)
    
    shutil.copy('app.bat', app_dir)
    shutil.copy('app.sh', app_dir)
    shutil.copy('run_app.R', app_dir)

    print('Done')


if __name__ == '__main__':
    main()