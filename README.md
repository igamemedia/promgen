# What is Promgen?

Promgen is a configuration file generator for [Prometheus](http://prometheus.io). Promgen is a web application written with [Django] and can help you do the following jobs.

* Create and manage Prometheus configuration files
* Configure alert rules and notification options

See the [Promgen introduction slides][Slides] for more details.

## Promgen screenshots


## Quickstart with Docker

Promgen attemps to use the [XDG] spec and follow suggestions for [12factor] apps

```bash
# Initialize required settings with docker container
docker run --rm --network host -v ~/.config/promgen:/etc/promgen/ promgen:latest bootstrap
# Apply database updates
docker run --rm --network host -v ~/.config/promgen:/etc/promgen/ promgen:latest migrate
```

You can then use your favorite configuration management system when deploying to each worker.

You should then configuration Prometheus to load the target file from Prometheus and configure AlertManager to send notifications back to Promgen.

See example settings files for proper configuration of Prometheus and AlertManager

* [Example settings file](promgen/tests/examples/promgen.yml)
* [Example prometheus file](docker/prometheus.yml)
* [Example alert manager file](docker/alertmanager.yml)

Assuming the settings have been properly copied to each node, you can run Promgen with the following commands

```bash
# Run Promgen web worker
docker run --rm --network host -p 8000:8000 -v ~/.config/promgen:/etc/promgen/ promgen:latest web

# Run Promgen celery worker
docker run --rm --network host -v ~/.config/promgen:/etc/promgen/ -v /etc/prometheus:/etc/prometheus promgen:latest worker
```

## Installing Promgen for Development

Promgen strives to be a standard Django application, so standard Django development patterns should apply

```bash
virtualenv --python=/path/to/python3 /path/to/virtualenv
source /path/to/virtualenv/activate
pip install -e .[dev]
pip install mysqlclient # psycopg or another database driver
# Setup database and update tables
promgen migrate
# Run tests
promgen test
# Run development server
promgen runserver
```


[12factor]: https://12factor.net/
[Django]: https://docs.djangoproject.com/en/1.10/
[Slides]: http://www.slideshare.net/tokuhirom/promgen-prometheus-managemnet-tool-simpleclientjava-hacks-prometheus-casual
[XDG]: https://specifications.freedesktop.org/basedir-spec/latest/ar01s03.html
