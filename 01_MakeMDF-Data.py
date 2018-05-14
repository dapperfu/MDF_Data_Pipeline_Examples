

import redis
import configparser
import rq

import make_data

def distributed_data_gen():
    config = configparser.ConfigParser()
    config.read('config.ini')
    r = redis.StrictRedis(
        host=config["redis"]["host"],
        port=config["redis"]["port"],
        db=config["redis"]["rq"],
    )
    q = rq.Queue(connection=r)
    for idx in range(1000):
        try:
            f = q.enqueue(make_data.random_data)
            print("{:04d}: {}".format(idx, f))
        except KeyboardInterrupt:
            print("\n\nCanceled\n\n")
            break
        except:
            raise

def local_data_gen():
    for idx in range(1000):
        try:
            file = make_data.random_data()
            print("{:04d}: {}".format(idx, file))
        except KeyboardInterrupt:
            print("\n\nDone\n\n")
            break

if __name__ == "__main__": 
    local_data_gen()
