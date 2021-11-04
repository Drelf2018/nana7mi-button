import os
import pydub
import file2json


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


def modifyAll():
    for root, folders, files in os.walk('./public/voices'):
        for file in files:
            sound = pydub.AudioSegment.from_file(os.path.join(root, file), "mp3")
            normalized_sound = match_target_amplitude(sound, -25.0)
            normalized_sound.export(os.path.join(root, file), format="mp3")
            print('已修改', file, '现音量', normalized_sound.dBFS)
        break


def view():
    for root, folders, files in os.walk('./public/voices'):
        for file in files:
            sound = pydub.AudioSegment.from_file(os.path.join(root, file), "mp3")
            print(os.path.join(root, file), sound.dBFS)


modifyAll()
# view()
file2json.run()
input('修改完成')
