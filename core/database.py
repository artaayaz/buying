import psycopg2


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='arta',
            user='peyman',
            password='peyman'
        )
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT * from products;')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
