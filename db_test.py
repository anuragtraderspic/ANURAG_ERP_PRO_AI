import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="anurag_erp",
        user="postgres",
        password=input("Enter PostgreSQL Password: ")
    )

    print("\n✅ Database Connected Successfully")

    conn.close()

except Exception as e:
    print("\n❌ Connection Failed")
    print(e)