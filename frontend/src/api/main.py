# api/main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from identity_generator import IdentityGenerator

app = Flask(__name__)
CORS(app)

@app.route('/api/generate-identity', methods=['POST'])
def generate_identity():
    try:
        data = request.json
        generator = IdentityGenerator(
            culture=data.get('culture', 'christian'),
            password_length=data.get('passwordLength', 16)
        )
        identity = generator.create_identity()
        return jsonify(identity)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/create-gmail', methods=['POST'])
def create_gmail():
    try:
        data = request.json
        generator = IdentityGenerator(
            culture=data.get('culture', 'christian'),
            password_length=data.get('passwordLength', 16)
        )
        # Set the identity if provided
        if 'identity' in data:
            generator.identity = data['identity']
        
        success = generator.create_gmail_account(
            headless=data.get('headless', False),
            recovery_email=data.get('recoveryEmail'),
            recovery_phone=data.get('recoveryPhone')
        )
        
        if success:
            # Save account details
            generator.save_account_details()
            return jsonify({
                'success': True,
                'message': 'Gmail account creation initiated successfully'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to create Gmail account'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)