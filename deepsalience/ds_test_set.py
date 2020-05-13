import utils
import config

import os
import subprocess


data_splits_path = os.path.join(config.data_save_folder, 'data_splits.json')
audio_path = '/scratch/hc2945/data/audiomixtures'
_, _, test_set = utils.load_json_data(data_splits_path)

for fname in test_set:

    audio_fpath = os.path.join(audio_path, fname)
    task = 'multif0'
    save_dir = '/scratch/hc2945/data/deepsalience_output'
    output_format = 'multif0'

    call_string = "python predict_on_audio.py {} {} {} -f {}".format(
        audio_fpath, task, save_dir, output_format
    )

    subprocess.call(call_string)
