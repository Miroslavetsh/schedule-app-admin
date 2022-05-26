from werkzeug.exceptions import NotFound

from config import db as client


def get_all(collection_name):
    with client:
        return client.json().get(collection_name)


def get(collection_name, id):
    with client:
        for obj in get_all(collection_name):
            if str(id) == str(obj["id"]):
                return obj
    return None


def post(collection_name, obj):
    with client:
        print(collection_name, obj)
        # TODO: Redis Add
        # client.json().set(collection_name, obj=obj)
        return obj


def put(collection_name, id, obj):
    with client:
        if (get(collection_name, id) != None):
            print(collection_name, obj)
            # TODO: Redis Update or GET + POST
            # client.json().set(id, collection_name, obj)
            return obj
        else:
            raise NotFound('No such entity found with id=' + str(id))


def delete(collection_name, id):
    with client:
        if (get(collection_name, id) != None):
            # TODO: Redis delete
            # client.json().delete(id, collection_name)
            return {'success': True}
        else:
            raise NotFound('No such entity found with id=' + str(id))
