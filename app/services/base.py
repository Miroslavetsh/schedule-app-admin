from config import db as client


def get_all(collection_name):
    with client:
        return client.json().get(collection_name)


def get(collection_name, id):
    with client:
        for entity in client.json().get(collection_name):
            if str(id) == str(entity["id"]):
                return entity
            return None


def post(collection_name, entity):
    pass


def put(collection_name, id, entity):
    pass


def delete(collection_name, id):
    with client:
        client.delete(collection_name, id)
        return True
