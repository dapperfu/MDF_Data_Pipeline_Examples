#!/usr/bin/env python3
"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -h | --help
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""
import os
from datetime import datetime

import pony.orm
from pony.orm.core import EntityMeta

pony.orm.set_sql_debug(False)

db = pony.orm.Database()

db.bind(
    provider="mysql",
    host="mysql",
    user="mdf_indexer_user",
    passwd="mdf_indexer_pass",
    db="mdf_database",
)

try:
    pass
#    db.drop_all_tables(with_all_data=True)
except pony.orm.ERDiagramError:
    pass

import asammdf

# For Local Indexing.
class MDF(db.Entity):
    """MDF ORM Entity Fancy"""

    # Filesystem Bits.
    key = pony.orm.Required(str, unique=True,)
    last_modified = pony.orm.Optional(datetime, volatile=True)
    etag = pony.orm.Optional(str,)
    size = pony.orm.Optional(int,)
    size_mb = pony.orm.Optional(float,)
    storage_class = pony.orm.Optional(str,)
    type = pony.orm.Optional(str,)
    name = pony.orm.Optional(str,)

    # Pre-calculated bits.
    basename = pony.orm.Optional(str,)
    product = pony.orm.Optional(str,)
    company = pony.orm.Optional(str,)

    # ASAM MDF Bits.
    version = pony.orm.Optional(str,)
    channels = pony.orm.Set("Channel",)

    # Basename.
    basename = pony.orm.Optional(str,)
    channels = pony.orm.Set("Channel",)

    # Metadata
    product = pony.orm.Optional(str,)
    company = pony.orm.Optional(str,)

    def __repr__(self):
        return f"MDF<{self.id},{self.product},{self.company},Ch:{len(self.channels)}>"


class Channel(db.Entity):
    """Channel entity to represent a 
    
    """

    name = pony.orm.Required(str, unique=True,)
    mdfs = pony.orm.Set("MDF",)

    def __repr__(self):
        return f"Channel<{self.id},{self.name}>"


@pony.orm.db_session
def upsert(cls, get, set=None):
    """
    Interacting with Pony entities.

    :param cls: The actual entity class
    :param get: Identify the object (e.g. row) with this dictionary
    :param set: Additional fields to set if ```get``` returns nothing.
    :return:
    """
    # does the object exist
    assert isinstance(cls, EntityMeta), f"{cls} is not a database entity"

    # if no set dictionary has been specified
    set = set or {}
    if not cls.exists(**get):
        obj = cls(**set, **get)
        return obj
    else:
        # get the existing object
        obj = cls.get(**get)
        for key, value in set.items():
            obj.__setattr__(key, value)
        return obj

db.generate_mapping(create_tables=True)