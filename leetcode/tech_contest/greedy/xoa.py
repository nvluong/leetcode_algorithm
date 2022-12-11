class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

st1 = Student("a", 36, 1)
st2 = Student("b", 36, 1)
st3 = Student("a1", 35, 1)
st4 = Student("a2", 36, 2)

list_st = [st1, st2, st3, st4]

dict_test = {}
li = []
dict = {}
for st in list_st:
    name = st.name
    age = st.age
    id = st.id
    str_tmp = str(age)+str(id)
    dict[str_tmp] = st

print(dict)




