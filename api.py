from flask import Flask, jsonify, request
import csv
import io

app = Flask(__name__)

# In-memory storage for transactions
transactions = []

# Endpoint to add a transaction
@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    transactions.append(data)
    return jsonify({'message': 'Transaction added successfully'}), 201

# Endpoint to retrieve all transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions), 200

# Endpoint to calculate KPI metrics
@app.route('/kpis', methods=['GET'])
def get_kpis():
    total_transactions = len(transactions)
    total_amount = sum(t.get('amount', 0) for t in transactions)
    return jsonify({'total_transactions': total_transactions, 'total_amount': total_amount}), 200

# Endpoint to export transactions to CSV
@app.route('/export/csv', methods=['GET'])
def export_csv():
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['id', 'amount', 'description'])
    writer.writeheader()
    writer.writerows(transactions)
    output.seek(0)
    return (output.getvalue(), 200, {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment; filename=transactions.csv'})

if __name__ == '__main__':
    app.run(debug=True)