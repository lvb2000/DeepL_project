import os
import random
import shutil

episode_paths = ('epsiodes_path1',
                 'epsiodes_path2',
                 'epsiodes_path3',
                 'episode_path4'
                 )


def get_list_of_folders():
    folder_names = []
    for path in episode_paths:
        folders = os.listdir(path)
        # prepend the path to the filenames
        folders = [os.path.join(path, f) for f in files]
        folder_names.extend(folders)
    return folder_names


def mix_episodes():
    # Create a new folder to hold the combined files
    new_folder = 'combined_episodes'
    os.makedirs(new_folder, exist_ok=True)

    # Get a list of all subfolders
    subfolders = get_list_of_folders()

    # Iterate through each subfolder
    for folder in random.sample(subfolders, len(subfolders)):
        # Get a list of all files in the subfolder
        files = os.listdir(folder)

        # Randomly select a file from the list
        random_file = random.choice(files)

        # Copy the file to the new folder
        shutil.copy(os.path.join(folder, random_file), new_folder)


if __name__ == '__main__':
    mix_episodes()
