from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, select, func
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabela no banco de dados
Base.metadata.create_all(engine)

# depreciado - será removido em futuro release
# print(engine.table_names())

# investiga o esquema de banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())

with Session(engine) as session:
    giovani = User(
        name='giovani',
        fullname='Giovani Trevisol',
        address=[Address(email_address="giovani@email.com")]
    )

    sandy = User(
        name='sandy',
        fullname='Sandy Silva',
        address=[Address(email_address='sandy@emial.br'),
                 Address(email_address='sandyc@emial.org')]
    )

    patrick = User(name='patrick', fullname='Patrick Cardoso')

    # persist data into BD
    session.add_all([giovani, sandy, patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['giovani', 'sandy']))
print('\nRecuperando usuários a partir de condição de filtragem')
print(stmt)
for user in session.scalars(stmt):
    print(user)

print("==================================")

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando os endereços de e-mail de sandy')
print(stmt_address)
for address in session.scalars(stmt_address):
    print(address)

print("==================================")

stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

print("==================================")

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('\nTotal de instância em Use')
for result in session.scalars(stmt_count):
    print(result)
