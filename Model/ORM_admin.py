from TUBES.Model.base import *


class Admin(Base):
    __tablename__ = 'Yang punya kantin'

    id = Column(Integer, primary_key=True)
    nama = Column(String(50), index=True, unique=True)
    pw = Column(String(32), nullable=False)

    def __init__(self, nama, pw):
        self.nama = nama
        self.pw = pw
        session = ses()
        session.add(self)
        session.commit()
        session.close

    def all():
        session = ses()
        return session.query(Admin).all()
        session.close()


Base.metadata.create_all(db)

# Admin1 = Admin('Taukhid','masuk123')
# session.add(Admin1)
# session.commit()
