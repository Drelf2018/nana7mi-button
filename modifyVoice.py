import os
import pydub


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


for root, folders, files in os.walk('./public/voices'):
    for file in files:
        sound = pydub.AudioSegment.from_file(os.path.join(root, file), "mp3")
        print(os.path.join(root, file), sound.dBFS)
        # normalized_sound = match_target_amplitude(sound, -25.0)
        # normalized_sound.export(os.path.join(root, file), format="mp3")
