# Author: Israt Jahan Khan

import os
import shutil

# Path to the main folder
main_folder_path = r"C:\Users\israt\Downloads\Compressed\archive_13\ADNI-Screening-1.5T-AD-Complete\Preprocessed_Data"

# Destination folder to copy orig.mgz files
destination_folder = r"C:\Users\israt\Downloads\Compressed\archive_13\ADNI-Screening-1.5T-AD-Complete\Extract_AD"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for root, dirs, files in os.walk(main_folder_path):
    if "mri" in dirs:
        mri_folder = os.path.join(root, "mri")

        orig_mgz_path = os.path.join(mri_folder, "aparc.DKTatlas+aseg.deep.mgz")
        if os.path.exists(orig_mgz_path):
            # Get the name of the subfolder
            subfolder_name = os.path.basename(root)

            destination_filename = f"{subfolder_name}_aseg_deep.mgz"

            shutil.copy(orig_mgz_path, os.path.join(destination_folder, destination_filename))
