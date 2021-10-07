import os
import json


def func(name, vlist):
    return {
        "categoryName": name,
        "categoryDescription": {
            "zh-CN": cnname.get(name, name)
        },
        "voiceList": [
            {
                "name": voice.split('.')[0],
                "path": voice if name == 'root' else os.path.join(name, voice),
                "description": {
                    "zh-CN": voice.split('.')[0]
                }
            } for voice in vlist
        ]
    }


data = {
    "voices": []
}
cnname = {
    'root': '未分类',
}
path = './public/voices'

for root, folders, files in os.walk(path):
    break
data['voices'].append(func('root', files))

for folder in folders:
    for root, fds, fes in os.walk(os.path.join(path, folder)):
        break
    data['voices'].append(func(folder, fes))

with open('./src/voices.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4, ensure_ascii=False))
