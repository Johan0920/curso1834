def studentEntity(entity) -> dict:
    return {
        "id":str(entity["_id"]),
        "name":entity["name"],
        "lastname":entity["lastname"],
        "clave":entity["clave"]
    }

def studentsEntity(entity) -> list:
    return [studentEntity(item) for item in entity]