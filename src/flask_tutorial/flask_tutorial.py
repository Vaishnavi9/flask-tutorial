from flask import Flask, make_response, request

my_app = Flask("My first Application")

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


@my_app.route("/")
def hello_world():
    return "Hello World!"

@my_app.route("/no_content")
def no_content():
    return ({"message": "something"}, 204)


@my_app.route("/explicit")
def explicit():
    resp = make_response({"message": "something"})
    resp.status_code = 200
    return resp

@my_app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"data": data}, 200
        else:
            return {"message": "Data is empty"}, 404
    except NameError:
        return {"message": "Data is not defined"}, 500

@my_app.route("/name_search")
def name_search():
    query = request.args.get('q')

    if query is None:
        return {"message": "Query parameter 'q' is required"}, 400

    if query.strip() == "" or query.isdigit():
        return {"message": "Query parameter 'q' cannot be empty or numeric"}, 400

    for person in data:
        if query.lower() in person["first_name"].lower():
            return {"data": person}, 200

    return {"message": "No person found with that first name"}, 404

@my_app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
    return {"message": "Person not found"}, 404

@my_app.route("/person/<uuid:id>", methods=["DELETE"])
def delete_person(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message": "Person deleted successfully"}, 200
    return {"message": "Person not found"}, 404

@my_app.route("/count")
def count():
    try:
        return {"count": len(data)}, 200
    except NameError:
        return {"message": "Data is not defined"}, 500


def main():
    my_app.run(debug=True)


if __name__ == "__main__":
    main()
