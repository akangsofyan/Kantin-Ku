from TUBES.Model.base import *
# from TUBES.Model.ORM_Menu import Menu

class Akun(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), index=True)
    password = Column(String(32), nullable=False)
    alamat = Column(String(50), nullable=False)
    tgl_lahir = Column(String(16), nullable=False)
    kontak = Column(String(16), nullable=False)
    job = Column(String(16), nullable=False)
    # child = relationship('Menu')

    def __init__(self,username,password,alamat,tgl_lahir,kontak,job):
        self.username = username
        self.password = password
        self.alamat = alamat
        self.tgl_lahir = tgl_lahir
        self.kontak = kontak
        self.job = job
        session = ses()
        session.add(self)
        session.commit()
        session.close()

    def all():
        session = ses()
        return session.query(Akun).all()
        session.close()

    def delete(id):
        session = ses()
        session.query(Akun).filter_by(user_id=id).delete()
        session.commit()
        session.close()

class Menu(Base):
    __tablename__='Daftar menu'

    id_menu = Column(Integer(), primary_key=True)
    id_penjual = Column(Integer(), ForeignKey('Users.user_id'))
    nama_menu = Column(String(32), nullable=False)
    harga_menu = Column(Integer(), nullable=False)
    stok = Column(Integer(), nullable=False)


    akun = relationship('Akun', backref=backref('Daftar menu'))

    # def __init__(self,user_id,username,password,alamat,tgl_lahir,kontak,job):
    #     self.user_id = user_id
    #     self.username = username
    #     self.password = password
    #     self.alamat = alamat
    #     self.tgl_lahir = tgl_lahir
    #     self.kontak = kontak
    #     self.job = job

Base.metadata.create_all(db)


