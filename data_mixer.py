import os
import random
import shutil
import numpy as np

episode_paths = ('mlruns/0/ccdce7a6a4964b5fbc6a64b6357877c4/artifacts/episodes/0',
                 'mlruns2/0/ccdce7a6a4964b5fbc6a64b6357877c4/artifacts/episodes/0'
                 )
batch_size = 10

def get_list_of_folders():
    folder_names = []
    for path in episode_paths:
        files = os.listdir(path)
        # prepend the path to the filenames
        file_path = [os.path.join(path, f) for f in files]
        folder_names.extend(file_path)
    return folder_names


def mix_episodes():
    # Create a new folder to hold the combined files
    new_folder = 'combined_episodes'
    os.makedirs(new_folder, exist_ok=True)

    # Get a list of all subfolders
    files_paths = get_list_of_folders()

    # Iterate through each subfolder
    # Init empty batch
    new_batch = []
    for idx in range(batch_size):
        # Get random file
        file = random.choice(files_paths)
        # Get batch of episodes
        batch = np.load(file)

if __name__ == '__main__':
    mix_episodes()
