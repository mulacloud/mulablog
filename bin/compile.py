from glob import glob
import shutil
import json

BASE_COMP = "src/Contents/"
DATA_PATH = "public/data/"
TARGET = "public/index.json"
CUT = 50

if __name__ == "__main__":
    result = []
    for a in glob("%s*.json" % BASE_COMP):
        file_name = int(a.split(BASE_COMP)[1].split(".")[0])
        shutil.copy(a, DATA_PATH + str(file_name) + ".json")
        data = json.loads(open(a, "r").read())
        content = data['content']
        if len(content) > CUT:
            data['content'] = content[0:CUT] + " ..."
        print(data)
        result.append(data)
    with open(TARGET, "w") as tg:
        tg.write(json.dumps(result))


