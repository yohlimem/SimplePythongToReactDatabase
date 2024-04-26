# CRUD create read update delete
from flask import request, jsonify
from config import app, db
from models import Contact
# read
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()  # get all contacts from the database
    json_contacts = list(map(lambda x: x.to_json(), contacts))  # convert contacts to json
    return jsonify({"contacts": json_contacts})  # return json response

# create
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    email = request.json.get("email")
    
    if not first_name or not email:
        return jsonify({"message": "You must include frist name and email"}), 400
    
    new_contact = Contact(first_name=first_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Contact created successfully"}), 201

# update
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)  # get contact by id from the database

    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)  # if firstName exists in request update it if it doesn't keep the old value
    contact.email = data.get("email", contact.email)  # if email exists in request update it if it doesn't keep the old value
    db.session.commit()  # commit changes to the database
    return jsonify({"message": "Contact updated successfully"})


# delete
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({"message": "Contact deleted successfully"})


if __name__ == "__main__":
    with app.app_context():  # wher we start the app get context of app
        db.create_all()  # create all tables in the database
    app.run(debug=True)
