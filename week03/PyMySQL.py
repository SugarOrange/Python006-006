#使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间将 ORM、插入、查询语句作为作业内容提交
class Student_table(Base):
    __tablename__ = 'student'

    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True)
    age = Column(Integer(), nullable=False)
    birthday = Column(DateTime())
    sex = Column(Boolean(), nullable=False)
    edu = Column(Enum("中学", "专科","本科", "硕士", "博士"))
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)

    def __repr__(self):
        return f'id={self.id}, name={self.name}, age={self.age}, ' \
               f'birthday={self.birthday}, sex={self.sex}, edu={self.edu}, ' \
               f'create_on={self.create_on}, update_on={self.update_on}'
student = Student_table(name='Jove',
                        age=18,
                        birthday=datetime(2002, 1, 1),
                        sex=True,
                        edu="本科",
                        )
session.add(student)
result = session.query(Student_table).filter(Student_table.name=='Jove').all()
print(result)
session.commit()
def insert_many():
    SQL = """INSERT INTO student (name, age, birthday, sex, edu, create_on, update_on)
    values (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        ('Peter', '22', datetime(1998,1,1), 1, '本科', datetime.now(), datetime.now()),
        ('Mary', '27', datetime(1993, 1, 1), 0, '硕士', datetime.now(), datetime.now()),
        ('Sor', '35', datetime(1985, 1, 1), 0, '博士', datetime.now(), datetime.now())
    )
    with db.cursor() as cursor:
        cursor.executemany(SQL, values)
    db.commit()

def read():
    SQL = """SELECT * FROM student WHERE name=%s"""
    with db.cursor() as cursor:
        cursor.execute(SQL, 'Peter')
        result = cursor.fetchall()
        print(result)
    db.commit()