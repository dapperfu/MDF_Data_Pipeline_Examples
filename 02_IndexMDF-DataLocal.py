# # PonyORM MDF Indexer
# ### Imports
# In[1]:
import os
import time

import asammdf
import get_files
import py
import pony.orm

from mdf_models import *

# # Database Setup

# In[2]:


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
        # make new object
        return cls(**set, **get)
    else:
        # get the existing object
        obj = cls.get(**get)
        for key, value in set.items():
            obj.__setattr__(key, value)
        return obj


@pony.orm.db_session
def index_data_file(data_file):
    """Index ASAMMDF Data File

    :param data_file: Path to ASAM MDF data file
    :return MDF: PonyORM MDF class
    """
    data_file_ = py.path.local(path=data_file,)

    mdf = asammdf.MDF(data_file)

    channels = list()
    mdf.channels_db.keys()
    for channel in mdf.channels_db.keys():
        channel_ = upsert(Channel, {"name": channel})
        channels.append(channel_)

    sha256 = data_file_.computehash(hashtype="sha256",)

    MDF_ = upsert(
        cls=MDF,
        get={"sha256": sha256},
        set={
            "name": data_file_.basename,
            "path": str(data_file_),
            "version": mdf.version,
            "size": data_file_.size(),
            "size_mb": data_file_.size() / 1024 ** 2,
            "atime": data_file_.atime(),
            "channels": channels,
        },
    )
    db.commit()

    return MDF_


if __name__ == "__main__":
    data_files = get_files.get_files(
        directory="Data/", extensions=[".mdf", ".mf4"],
    )

    t1 = time.time()
    for idx, data_file in enumerate(data_files):
        print(f"Indexing {idx:04d}: {data_file}")
        index_data_file(data_file=data_file,)
    t2 = time.time()

    print("Elapsed Indexing Time: {}".format(t2 - t1))
