from flask import Flask, request, jsonify
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'pingStats')
DB_USER = os.getenv('DB_USER', 'pingStats')
DB_PASS = os.getenv('DB_PASS', 'pingStats')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/uptime')
def uptime():
    up_value = request.args.get('up', default=1, type=int)
    user_agent = request.headers.get('User-Agent', 'unknown')
    timestamp = datetime.utcnow()

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO uptime (\"when\", who, value) VALUES (%s, %s, %s)",
            (timestamp, user_agent, up_value)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"up": up_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
