from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample fraud detection engine
class FraudDetectionEngine:
    def __init__(self):
        pass

    def detect_fraud(self, transaction_data):
        # Placeholder for fraud detection logic
        # In a real scenario, this would involve machine learning models or heuristics
        if transaction_data['amount'] > 10000:  # Example threshold
            return True
        return False

fraud_detection_engine = FraudDetectionEngine()

@app.route('/api/transaction', methods=['POST'])
def transaction():
    transaction_data = request.get_json()
    is_fraudulent = fraud_detection_engine.detect_fraud(transaction_data)
    return jsonify({'is_fraudulent': is_fraudulent})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'running'}), 200

if __name__ == '__main__':
    app.run(debug=True)