import click
import redis
import configparser
import rq

import make_data

def distributed_data_gen(n=1, *args, **kwargs):
    config = configparser.ConfigParser()
    config.read('config.ini')
    r = redis.StrictRedis(
        host=config["redis"]["host"],
        port=config["redis"]["port"],
        db=config["redis"]["rq"],
    )
    q = rq.Queue(connection=r)
    for idx in range(n):
        try:
            f = q.enqueue(make_data.random_data)
            print("{:04d}: {}".format(idx, f))
        except KeyboardInterrupt:
            print("\n\nCanceled\n\n")
            break
        except:
            raise

def local_data_gen(n=1, *args, **kwargs):
    for idx in range(n):
        try:
            file = make_data.random_data()
            print("{:04d}: {}".format(idx, file))
        except KeyboardInterrupt:
            print("\n\nDone\n\n")
            break

@click.command()
@click.option('--distribute/--no-distribute', default=False)
@click.option('--N', default=1, show_default=True)
def hello(distribute, **kwargs):
#    print(kwargs)
    if distribute:
        distributed_data_gen(**kwargs)
    else:
        local_data_genInfluxDB Python Examples
(**kwargs)


if __name__ == '__main__':
    hello()
