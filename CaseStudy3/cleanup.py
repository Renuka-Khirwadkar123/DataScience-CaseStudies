# Folder Cleanup – Keep only original and final cleaned dataset
import os
import glob

folder_path = "../CaseStudy3"
files_to_keep = {
    os.path.abspath(os.path.join(folder_path, "SuperStore_Dataset.csv")),
    os.path.abspath(os.path.join(folder_path, "SuperStore_Final_Dataset.csv"))
}

# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Delete all except the files to keep
for file in csv_files:
    file_path = os.path.abspath(file)
    if file_path not in files_to_keep:
        os.remove(file_path)
        print(f"Deleted: {file}")
    else:
        print(f"Kept: {file}")
