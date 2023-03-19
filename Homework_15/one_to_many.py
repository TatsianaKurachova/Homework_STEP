"""
Используя sqlAlchemy создать базу и несколько таблиц (любые)
реализовать связь Один ко многим

"""
from sqlalchemy.orm import DeclarativeBase, Session, relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey

# движок
db = 'sqlite:///one_to_many.db'
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
    pupils= relationship("Pupil", back_populates = "teacher")
 

class Pupil(Base):
    __tablename__ = "pupils"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates = "pupils")
      

Base.metadata.create_all(bind=engine)


with Session(autoflush=False, bind=engine) as view:
   
    anna = Teacher(name='Anna')
    alla = Teacher(name='Alla')
      
    alex = Pupil(name='Alex')
    phil = Pupil(name='Phil')
    artem = Pupil(name='Artem')
    tati = Pupil(name='Tati')
    nata = Pupil(name='Nata')

    anna.pupils=[nata, tati]
    alla.pupils = [artem, phil]
    
    view.add_all([anna, alla])
    view.commit()

    query = view.query(Teacher, Pupil)
    query = query.outerjoin(Teacher, Teacher.id == Pupil.teacher_id)
    records = query.all()
    print(records)
   
		



    


