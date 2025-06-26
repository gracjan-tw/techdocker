from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydb",
            user="myuser",
            password="mypassword"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM messages;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
