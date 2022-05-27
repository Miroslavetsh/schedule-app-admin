from werkzeug.exceptions import NotFound
from redis.commands.json.path import Path

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
        client.json().arrappend(collection_name, Path.root_path(), obj)
        return obj


def put(collection_name, obj):
    id = obj["id"]

    with client:
        if (get(collection_name, id) != None):
            delete(collection_name, id)
            post(collection_name, obj)
            return obj
        else:
            raise NotFound('No such entity found with id=' + str(id))


def delete(collection_name, id):
    with client:
        if (get(collection_name, id) != None):
            collection = get_all(collection_name)

            for entity in collection:
                if entity['id'] == id:
                    collection.remove(entity)

            client.json().set(collection_name, Path.root_path(), collection)

            return {'success': True}
        else:
            raise NotFound('No such entity found with id=' + str(id))
