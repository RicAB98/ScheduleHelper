import json
from Class import Class
from Subject import Subject

class JsonHelper:
    def ConvertTo(subjects):
        dictionary = {
            "subjects": []
        }

        for s in subjects:
            subjectJson = {
                "name": s.name,
                "classes": []
            }

            for c in s.classes:
                subjectJson["classes"].append({
                    "day": c.day,
                    "start": c.start,
                    "end": c.end,
                    "name": c.name
                })

            dictionary["subjects"].append(subjectJson)

        with open(f'horario.json', 'w') as f:
            json.dump(dictionary, f)

    def Parse(file):
        f = open(file)
        data = json.load(f)
        
        subjects = data["subjects"]
        result = []
        index = 0

        for s in subjects:
            classes = []

            for c in s["classes"]:
                classText = f'{c["day"]} - {c["start"]} - {c["end"]} ({c["name"]})'

                classes.append(classText) 

            result.append(Subject(index, s["name"], classes))
            index += 1
            
        return result