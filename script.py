import os
import shutil

def detect_and_save_files(main_folder_path, output_folder):
    """
    Function to detect specific files in subfolders and copy them to the output folder.

    Args:
        main_folder_path (str): Path to the main folder containing subfolders.
        output_folder (str): Path to the output folder where files will be copied.

    Returns:
        None
    """
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Walk through the main folder and its subfolders
    for root, dirs, files in os.walk(main_folder_path):
        # Check if there is a 'mri' folder in the current directory
        if "mri" in dirs:
            # Get the path to the 'mri' folder
            mri_folder = os.path.join(root, "mri")

            # Check if the file exists in the 'mri' folder
            orig_mgz_path = os.path.join(mri_folder, "aparc.DKTatlas+aseg.deep.mgz")
            if os.path.exists(orig_mgz_path):
                # Get the name of the subfolder
                subfolder_name = os.path.basename(root)

                # Create a destination filename
                destination_filename = f"{subfolder_name}_aseg_deep.mgz"

                # Copy the file to the output folder
                shutil.copy(orig_mgz_path, os.path.join(output_folder, destination_filename))

def main():
    # Define the paths to main folder and output folders
    main_folder_path = r"C:\Users\israt\Desktop\FYDP\Preprocessed"
    ad_output_folder = r"C:\Users\israt\Desktop\FYDP\Extracted_AD"
    mci_output_folder = r"C:\Users\israt\Desktop\FYDP\Extracted_MCI"
    cn_output_folder = r"C:\Users\israt\Desktop\FYDP\Extracted_CN"

    # Detect and save files for AD, MCI, and CN
    detect_and_save_files(os.path.join(main_folder_path, "AD"), ad_output_folder)
    detect_and_save_files(os.path.join(main_folder_path, "MCI"), mci_output_folder)
    detect_and_save_files(os.path.join(main_folder_path, "CN"), cn_output_folder)

if __name__ == "__main__":
    main()
