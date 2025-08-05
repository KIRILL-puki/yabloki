# u = "kavalkir"
# p = "PZlOXmNns8q4i03w"


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kavalkir:PZlOXmNns8q4i03w@cluster0.cjujal6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['books_db']
collection = db['books']

book1 = {
    "название": "Гра престолів",
    "цена": 300,
    "год выпуска": 1996,
    "количество страниц": 694
}

school_books = [
    {"название": "Історія України", "класс": 7, "количество страниц": 210},
    {"название": "Алгебра", "класс": 7, "количество страниц": 180},
    {"название": "Географія", "класс": 7, "количество страниц": 160},
    {"название": "Фізика", "класс": 7, "количество страниц": 220},
    {"название": "Українська література", "класс": 7, "количество страниц": 250}
]
collection.insert_many(school_books)
collection.insert_one(book1)