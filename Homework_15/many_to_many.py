
"""
Используя sqlAlchemy создать базу и несколько таблиц (любые)
реализовать связь Многое ко многим

"""

from sqlalchemy.orm import DeclarativeBase, Session, relationship 
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table, MetaData, Select

# движок
db = 'sqlite:///many_to_many.db'
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
    

class Pupil(Base):
    __tablename__ = "pupils"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
      
class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), autoincrement=True)
    pupil_id = Column(Integer, ForeignKey("pupils.id"), autoincrement=True)


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

    math = Lesson(name = "Math", teacher_id="3", pupil_id = "7")
    phisic = Lesson(name = "Phisic", teacher_id="1", pupil_id = "2")
    
    

    view.add_all([alex, phil, artem, tati, nata, anna, alla, ben, kirill, ed, math, phisic])
    view.commit() 
    query = view.query(Teacher, Pupil, Lesson)
    query = query.outerjoin(Lesson, Lesson.id == Pupil.id)
    records = query.all()
    print(records)
    
    

    



    

