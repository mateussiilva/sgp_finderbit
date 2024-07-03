from faker import Faker
import sqlite3


conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()
fake = Faker("pt-br")
name_table = "clientes_cliente"


def prencher():
    for n in range(10):
        name = fake.name()
        phone = fake.phone_number()
        cep = fake.postcode()
        cur.execute("""
                    INSERT INTO clientes_cliente
                    (name, telephone,cep)
                    VALUES(?,?,?)
                    
                    """,
                    (name, phone, cep))
        # print(data)
        conn.commit()

prencher()

# clientes = cur.execute("SELECT * FROM clientes_cliente")
# for cliente in clientes:
#     cur.execute(
#         f"""DELETE FROM {name_table}
#         WHERE id_client = ?
#         """,
#         (cliente[0],)
#     )
# conn.commit()
cur.close()
conn.close()
