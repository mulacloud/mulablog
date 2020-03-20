from glob import glob
import shutil
import json

BASE_COMP = "src/Contents/"
DATA_PATH = "public/data/"
TARGET = "public/index.json"
CUT = 70

def parse_data(data):
    key = None
    value = None
    end = False
    result = {}
    for item in data.readlines():
        if item.startswith("# "):
            key = item.replace("#","").strip()
            result[key] = None
            end = False
        elif item.startswith("##"):
            key = None
            end = True
        elif key and not end:
            value = item.replace("\n","").strip()
            old_value = result[key]
            if old_value:
                result[key] = old_value + " " + value
            else:
                result[key] = value

    return result

if __name__ == "__main__":
    result = []
    for a in glob("%s*.txt" % BASE_COMP):
        file_name = int(a.split(BASE_COMP)[1].split(".")[0])
        data = parse_data(open(a, "r"))
        data['id'] = int(file_name)
        with(open(DATA_PATH + "%s.json" % file_name, 'w')) as js:
            js.write(json.dumps(data))
        content = data['content']
        if len(content) > CUT:
            data['content'] = content[0:CUT] + " ..."
        print(data)
        result.append(data)
    with open(TARGET, "w") as tg:
        tg.write(json.dumps(result))


