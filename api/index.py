import json
import os

# Load JSON data once (on cold start)
with open(os.path.join(os.path.dirname(__file__), 'data.json')) as f:
    STUDENT_DATA = json.load(f)

def handler(request, response):
    names = request.query.get("name", [])

    if isinstance(names, str):
        names = [names]

    result = {"marks": []}
    for name in names:
        for entry in STUDENT_DATA:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"
    return response.send(json.dumps(result))