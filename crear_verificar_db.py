import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def verificar_conexion():
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="user_almacen",
            password="password_seguro_123",
            database="almacen"
        )
        print("✅ Conexión a PostgreSQL exitosa")

        # Verificar que la base de datos existe y tenemos acceso
        cursor = conn.cursor()
        cursor.execute("SELECT current_database(), current_user;")
        db_info = cursor.fetchone()
        print(f"✅ Conectado a: {db_info[0]} como usuario: {db_info[1]}")

        cursor.close()
        conn.close()
        return True

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        print("\n🔧 Solución:")
        print("1. Verifica que PostgreSQL esté ejecutándose")
        print("2. Confirma que la BD 'almacen' existe")
        print("3. Verifica usuario 'user_almacen' y password")
        return False

if __name__ == "__main__":
    verificar_conexion()
