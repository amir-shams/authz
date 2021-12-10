from uuid import uuid4

def uuidgen():
    """
    Generate new UUID for resources id filed in database.
    """
    return uuid4().hex