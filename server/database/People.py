from model.User.User import User
from utils.toJSON import toJSON

people = toJSON([
    User("k@.ua", "John", "2323"),
    User("m@.ua", "Mike", "1241"),
    User("b@i.ua", "Bob", "1242"),
    User("d@i.ua", "Doe", "42112")
])


print(people)
