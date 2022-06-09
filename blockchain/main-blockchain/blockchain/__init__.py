#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("BLOCKCHAIN_TYPE_STORAGE")

if storage_t == "db":
    from blockchain.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from blockchain.engine.file_storage import FileStorage
    storage = FileStorage()

loaded_chain = storage.reload()