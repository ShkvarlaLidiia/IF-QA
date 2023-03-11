from pymongo import MongoClient


def connection():
    CONNECTION_STRING = "mongodb+srv://user:2211@cluster.nulzyqw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)

    return client['data']

    # for doc in data_collection.find():
    #     print(doc)


# def insert_data_to_db():
#     data = get_data()

#     data_collection = data['users']

#     amount_of_user = data_collection.count_documents({"name": "John"})

#     if amount_of_user > 0:
#         raise NameError(
#             f"There is {amount_of_user} user , mend it other way!"
#         )

#     data_collection.insert_one(person)
