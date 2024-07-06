import os
import shutil
import argparse
from pathlib import Path

def copy_artwork(launchbox_dir, dest_dir):
    precedence = ["United States", "North America", "World"]
    
    for platform in os.listdir(os.path.join(launchbox_dir, 'Images')):
        platform_path = os.path.join(launchbox_dir, 'Images', platform)
        
        if os.path.isdir(platform_path):
            for art_type in os.listdir(platform_path):
                art_type_path = os.path.join(platform_path, art_type)
                
                if os.path.isdir(art_type_path):
                    files_to_copy = []
                    
                    # First check for specific countries
                    for region in precedence:
                        region_path = os.path.join(art_type_path, region)
                        if os.path.isdir(region_path):
                            files_to_copy.extend([os.path.join(region_path, f) for f in os.listdir(region_path)])
                    
                    # Then check the root of the art type folder
                    files_to_copy.extend([os.path.join(art_type_path, f) for f in os.listdir(art_type_path) if os.path.isfile(os.path.join(art_type_path, f))])
                    
                    # Finally, check for any other folders
                    for folder in os.listdir(art_type_path):
                        other_folder_path = os.path.join(art_type_path, folder)
                        if os.path.isdir(other_folder_path) and folder not in precedence:
                            files_to_copy.extend([os.path.join(other_folder_path, f) for f in os.listdir(other_folder_path)])
                    
                    # Create the destination directory
                    dest_platform_art_type_dir = os.path.join(dest_dir, platform, art_type)
                    Path(dest_platform_art_type_dir).mkdir(parents=True, exist_ok=True)
                    
                    # Copy files to the appropriate destination directory
                    for file in files_to_copy:
                        if os.path.isfile(file):
                            print(f"Copying {file}")
                            shutil.copy(file, dest_platform_art_type_dir)

def main():
    parser = argparse.ArgumentParser(description='Copy artwork from LaunchBox to a structured directory.')
    parser.add_argument('launchbox_dir', type=str, help='Path to the LaunchBox directory')
    parser.add_argument('dest_dir', type=str, help='Path to the destination directory')
    args = parser.parse_args()

    copy_artwork(args.launchbox_dir, args.dest_dir)

if __name__ == "__main__":
    main()
