import json
from Subject import Subject

class JsonHelper:
    def ConvertTo(subjects, fileName):
        dictionary = {
            "subjects": []
        }

        for s in subjects:
            subjectJson = {
                "name": s.name,
                "classes": []
            }

            index = 0

            for c in s.classes:
                classJson = {
                    "day": c.day,
                    "start": c.start,
                    "end": c.end,
                    "name": c.name,
                    "active": False
                }

                if index == s.comboBox.currentIndex():
                    classJson["active"] = True

                subjectJson["classes"].append(classJson)

                index += 1

            dictionary["subjects"].append(subjectJson)

        with open(f'{fileName}.json', 'w') as f:
            json.dump(dictionary, f)

    def Parse(file):
        f = open(file)
        data = json.load(f)
        
        subjects = data["subjects"]
        result = []
        index = 0

        for s in subjects:
            classes = []
            activeIndex = -1
            index = 0

            for c in s["classes"]:
                classText = f'{c["day"]} - {c["start"]} - {c["end"]} ({c["name"]})'

                if c["active"]:
                    activeIndex =  index   

                classes.append(classText) 

                index += 1

            s = Subject(index, s["name"], classes)
            s.comboBox.setCurrentIndex(activeIndex)
            result.append(s)
            index += 1
            
        return result