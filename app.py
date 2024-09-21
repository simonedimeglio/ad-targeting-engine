from flask import Flask, jsonify
from targeting_engine import AdTargetingEngine

# Initialize Flask application
app = Flask(__name__)

# Create an instance of the AdTargetingEngine
targeting_engine = AdTargetingEngine()

@app.route('/serve_ad/<user_id>')
def serve_ad(user_id):
    """
    API endpoint to serve an ad to a specific user.
    
    Args:
        user_id (str): The ID of the user requesting an ad.
    
    Returns:
        JSON response containing user data and the served ad.
    """
    result = targeting_engine.serve_ad(user_id)
    return jsonify(result)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    # Note: Debug mode should be turned off in a production environment
    app.run(debug=True)