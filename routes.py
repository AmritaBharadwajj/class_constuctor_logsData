# routes.py

from flask import Blueprint, request, jsonify
from .models import Activity 
from . import db  

activity_blueprint = Blueprint('activity', __name__)

@activity_blueprint.route('/store_activity', methods=['POST'])
def store_activity():
    data = request.json

    # Extract data from the JSON and create an Activity object
    activity = Activity(
        time=data['time'],
        unique_qualifier=data['unique_qualifier'],
        application_name=data['application_name'],
        customer_id = Column(String)
        actor_email = Column(String)
        actor_profile_id = Column(String)
        ip_address = Column(String)
        events = Column(JSON)
        
    )

   
    db.session.add(activity)

  
    db.session.commit()

    return jsonify({'message': 'Activity stored successfully'}), 201
