from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

# Declaration class to ORM Model
Base = declarative_base()


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(String(9), unique=True)
    address = Column(String(30))

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, address={self.address})"


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(2))
    agency = Column(Integer)
    number = Column(Integer)
    balance = Column(Float)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    def __repr__(self):
        return f"Account(id={self.id}," \
               f" type={self.tipo}, " \
               f"agency={self.agency}, " \
               f"number={self.number} ," \
               f"balance={self.balance})"


# create a connection with DB
engine = create_engine("sqlite://")

# Create all classes to tables into BD
Base.metadata.create_all(engine)

# Persist data
with Session(engine) as session:
    giovani = Client(name='Giovani Trevisol',
                     cpf='123.654.789.10',
                     address='Rua qualquer, nr 123'
                     )

    lara = Client(name='Lara Talita',
                  cpf='111.222.333.44',
                  address='Rua alguma coisa, nr 99'
                  )

    pedro = Client(name='Pedro da Silva',
                   cpf='888.999.666.77',
                   address='Rua seila, nr 899'
                   )

    account1 = Account(client_id='1',
                       tipo='cc',
                       agency=789,
                       number=980012,
                       balance=100001.86
                       )
    account2 = Account(client_id='2',
                       tipo='cp',
                       agency=123,
                       number=191109,
                       balance=299.91
                       )
    account3 = Account(client_id='3',
                       tipo='cc',
                       agency=567,
                       number=120841,
                       balance=4788.13
                       )

    # Persist data
    session.add_all([giovani, lara, pedro])
    session.add_all([account1, account2, account3])
    session.commit()

# query the database

print('Retrieving customers from conditions:')
stmt_clients = select(Client).where(Client.name.in_(['Giovani', 'Giovani Trevisol']))
for result in session.scalars(stmt_clients):
    print(result)

print("\nRetrieving customers in an orderly manner:")
stmt_order = select(Client).order_by(Client.name.desc())
for result in session.scalars(stmt_order):
    print(result)

print("\nRecovering accounts in an orderly manner:")
stmt_accounts = select(Account).order_by(Account.tipo.desc())
for result in session.scalars(stmt_accounts):
    print(result)

print("\nRecovering accounts and customers:")
stmt_join = select(Client.name, Account.tipo, Account.balance).join_from(Client, Account)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

session.close()
