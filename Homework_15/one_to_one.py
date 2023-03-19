"""
Используя sqlAlchemy создать базу и несколько таблиц (любые)
реализовать связь один к одному

"""
from sqlalchemy.orm import DeclarativeBase, Session, relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey

# движок
db = 'sqlite:///one_to_one.db'
engine = create_engine(db, echo=True)
engine.connect()

# базовый класс
class Base(DeclarativeBase):
    pass

# будущая таблица (модель)
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pupils= relationship("Pupil", back_populates = "teacher", uselist=False)
 

class Pupil(Base):
    __tablename__ = "pupils"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates = "pupils")
      

Base.metadata.create_all(bind=engine)


with Session(autoflush=False, bind=engine) as view:
  
    alex = Pupil(name='Alex')
    phil = Pupil(name='Phil')
    artem = Pupil(name='Artem')
    tati = Pupil(name='Tati')
    nata = Pupil(name='Nata')
        
    anna = Teacher(name='Anna')
    alla = Teacher(name='Alla')
    ben = Teacher(name='Ben')
    kirill = Teacher(name='Kirill')
    ed = Teacher(name='Ed')


    alex.teacher = anna
    phil.teacher = alla
    artem.teacher = ben
    tati.teacher = kirill
    nata.teacher = ed

    view.add_all([alex, phil, artem, tati, nata])
    view.commit() 
    query = view.query(Teacher, Pupil)
    records = query.all()
    print(records)

