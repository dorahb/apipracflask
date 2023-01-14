from flask import Flask, jsonify, request

app = Flask(__name__)

countries = [
    {"id":1 , "name": "India", "capital": "New Delhi","area": 3287263, "population": 1324171353},
    {"id":2 , "name": "China", "capital": "Beijing","area": 9596960, "population": 1403500365},
    {"id":3 , "name": "United States", "capital": "Washington, D.C.","area": 9629091, "population": 331002651},

]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)


@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return {"message": f"Country {country['name']} has been created successfully."}, 201
    else:
        return {"error": "The request payload is not in JSON format"}, 415
