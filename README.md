# Turnkey MDF Data Pipeline Examples

**Engineers**: It's some Python stuff. Index, process, and analyze your MDF files. Make use of the terabytes of data sitting on all those shared drives. Aggregate a lot of data, or mine a lot of data looking for one 15 ms flag event.
**Managers**: *Webscale data analytics commercial off-the-shelf opensource components*. *Edge Computing Data Analysis for Sensitive Data*.

## ```docker-compose```

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.
> \- https://docs.docker.com/compose/

- Jupyter Notebooks Analysis Environment
- mysql database
- Minio (S3)
- Redis (For rq)

#

    mc config host add mdf http://127.0.0.1:49000 mdf_minio_access_key mdf_minio_secret_key


   docker-compose logs -f s3_callback


Adminer:

   http://localhost:43307/

[http://rabbitmq_user:rabbitmq_pass@localhost:45673](http://rabbitmq_user:rabbitmq_pass@localhost:45673)


### Acknowledgments

#### Nanos Gigantum Humeris Insidentes

This project would not be possible without a multiple other existing projects, including but not limited to:

- [Python](https://www.python.org/): A programming language that lets you work quickly and integrate systems more effectively.
- [asammdf](https://github.com/danielhrisca/asammdf):  A fast parser and editor for ASAM (Associtation for Standardisation of Automation and Measuring Systems) MDF (Measurement Data Format) files.
- [Flask](http://flask.pocoo.org/): A microframework for Python based on Werkzeug, Jinja 2 and good intentions.
- [PonyORM](https://ponyorm.com/): A Python ORM with beautiful query syntax.

#### On n'est jamais servi si bien que par soi-même

This project would not have been necessary if it wasn't for current industry tools, including but not limited to:

- [DIAdem](http://www.ni.com/diadem): *Software specifically designed to "help" engineers and scientists quickly locate, inspect, analyze, and report on measurement data using one software tool.*
    - *Starting* at $1225
    - Visual Basic
