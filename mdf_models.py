import os

import pony.orm
from pony.orm.core import EntityMeta

pony.orm.set_sql_debug(False)

db = pony.orm.Database()

database_file = os.path.abspath("mdf_index.sqlite")

db.bind(
    provider="sqlite", filename=database_file, create_db=True,
)


class MDF(db.Entity):
    name = pony.orm.Required(str,)
    path = pony.orm.Required(str,)
    version = pony.orm.Required(str,)
    sha256 = pony.orm.Required(str,)
    size = pony.orm.Optional(float,)
    size_mb = pony.orm.Optional(float,)
    atime = pony.orm.Optional(float,)
    channels = pony.orm.Set("Channel",)


class Channel(db.Entity):
    name = pony.orm.Required(str, unique=True,)
    mdfs = pony.orm.Set("MDF",)


db.generate_mapping(create_tables=True)
