import mysql.connector


def get_connection():
    return mysql.connector.connect(
    host="localhost", user="root", password="kodkod", database="school")


def create_game():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS games(
                id INT AUTO_INCREMENT PRIMARY KEY,
                secret_code VARCHAR(100) NOT NULL,
                attempts_used  INT NOT NULL,
                status  VARCHAR(100)
                
                );
            """)
    finally:
        conn.close()

def add_game(secret_code, attempts_used, status):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO games (secret_code, attempts_used, status)
            VALUES(%s, %s, %s)
            """, (secret_code, attempts_used, status,))
        conn.commit()

    finally:
        conn.close()


def add_guesses(game_id, guess):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT secret_code, attempts_used, status
            FROM games
            WHERE id = %s;
            """, (game_id,))
        
        game =  cursor.fetchone()
        attempts_used = game["attempts_used "]
        status = game["status"]

        if status in ("won", "lost"):
            return 409
        if attempts_used >= 10:
            return 409
        
        secret_guess = guess["guess"]
        secret_code = list(game["secret_code"].split())
        if secret_guess[0] == secret_code[0] or secret_code[1] == secret_guess[1] or secret_guess[2] == secret_code[2] or secret_code[3] == secret_guess[3]:
            cursor.execute(
                """
                UPDATE games
                SET
                attempt_used += 1

                """
            )


    finally:
        conn.close()
