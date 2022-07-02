import json

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
                    "end": c.end
                })

            dictionary["subjects"].append(subjectJson)

        with open(f'horario.json', 'w') as f:
            json.dump(dictionary, f)
