import click
from app import create_app
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
@click.option("-h", "--host", default="0.0.0.0", help="The interface to bind to.")
@click.option("-p", "--port", default=5000, help="The port to bind to.")
@click.option("--debug/--no-debug", default=True, help="Enable or disable debug mode.")
@click.option("--reload/--no-reload", default=True, help="Enable or disable automatic reloading.")
@click.option("--workers", default=1, help="The number of worker processes.")
@click.option("--timeout", default=120, help="The worker timeout in seconds.")
@click.option("--max-requests", default=0, help="The maximum number of requests per worker process.")
@click.option("--access-log/--no-access-log", default=True, help="Enable or disable access log.")
@click.option("--worker-class", default="gevent", help="Define worker class to use with gunicorn")
def run_server(host, port, debug, reload, workers, timeout, max_requests, access_log, worker_class):
    """Run the Flask server."""
    options = {
        "bind": f"{host}:{port}",
        "workers": workers,
        "worker_class": worker_class,
        "timeout": timeout,
        "max_requests": max_requests,
        "accesslog": "-" if access_log else None,
        "reload": reload,
        "debug": debug,
    }
    from gunicorn.app.base import BaseApplication
    class FlaskApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()
        
        # overriding the parent method
        def load_config(self):
            for k, v in self.options.items():
                if k in self.cfg.settings and v is not None:
                    self.cfg.set(k.lower(), v)
        
        # overriding the parent method
        def load(self):
            return self.application
    
    FlaskApplication(app, options).run()
                    

@cli.command
def test():
    """Run the tests."""
    click.echo("Running tests...")


if __name__ == "__main__":
    cli()