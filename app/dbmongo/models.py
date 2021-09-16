from mongoengine import *
from app import db


class Mensaje(Document):
    ts = FloatField()
    texto = StringField()

    def _init__(self, ts, texto):
        self.texto = texto
        self.ts = ts


"""
    #url_db = os.environ.get("DATABASE_URL")
    #print("Datos de la BD:")
    # print(url_db)
    ts = time.time()
    #myclient = pymongo.MongoClient(url_db)
    #myclient = pymongo.MongoClient("mongodb://mongodb-26-rhel7:27017/")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["pythonlog"]
    mycol = mydb["logs"]
    myclient.close()

    print("Datos de la BD:")
    # print(url_db)
    print(mydb)
    print(mycol)
    print(ts)
    mydict = {"hora": ts}
    x = mycol.insert(mydict)
    #xx = mycol.insert_one(mydict)
    # mycol.insert_one()

    mistring = "Inserto en " + mydb.name + " " + mycol.name + "a las "
    print(mistring)
    print(ts)

   
    class Mongo(Resource):
        def post(self):
            postedData = request.get_json()
            nom = postedData["Nombre"]
            eda = postedData["Edad"]
            mydict = {"name": nom, "Edad:": eda}
            x = mycol.insert(mydict)
            #x = mycol.insert_one(mydict)
            retMap = {
                'Mongo return': mistring,
                'Status code': 200
            }
            return jsonify(retMap)
   """
