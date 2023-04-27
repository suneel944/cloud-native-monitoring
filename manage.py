from gevent import monkey

monkey.patch_all()

from flask_script import Manager, Server as _Server, Option
from src.app import create_app

manager = Manager(create_app)

class Server(_Server):
    # Custom Flask server class that extends the default Flask server class _Server

    help = description = "Runs the Flask web server"

    # Help and description messages for the command-line interface

    def get_options(self):
        # Define the command-line options for the Flask server
        options = (
            Option("-h", "--host", dest="host", default=self.host),
            # Host address for the server
            Option("-p", "--port", dest="port", type=int, default=self.port),
            # Port number for the server
            Option(
                "-d",
                "--debug",
                action="store_true",
                dest="use_debugger",
                help=(
                    "enable the Werkzeug debugger (DO NOT use in " "production code)"
                ),
                default=self.use_debugger,
            ),
            # Enable the Werkzeug debugger
            Option(
                "-D",
                "--no-debug",
                action="store_false",
                dest="use_debugger",
                help="disable the Werkzeug debugger",
                default=self.use_debugger,
            ),
            # Disable the Werkzeug debugger
            Option(
                "-r",
                "--reload",
                action="store_true",
                dest="use_reloader",
                help=(
                    "monitor Python files for changes (not 100%% safe "
                    "for production use)"
                ),
                default=self.use_reloader,
            ),
            # Enable auto-reloading of the server on code changes
            Option(
                "-R",
                "--no-reload",
                action="store_false",
                dest="use_reloader",
                help="do not monitor Python files for changes",
                default=self.use_reloader,
            ),
            # Disable auto-reloading of the server on code changes
        )
        return options

    def __call__(self, app, host, port, use_debugger, use_reloader):
        # Override the default behavior of the _Server class to start a Flask server

        if use_debugger is None:
            use_debugger = app.debug
            if use_debugger is None:
                use_debugger = True
        # If use_debugger is not set explicitly, use the app's debug setting
        # If the app's debug setting is not set, default to True

        if use_reloader is None:
            use_reloader = app.debug
        # If use_reloader is not set explicitly, use the app's debug setting

        app.run(
            host=host,
            port=port,
            debug=use_debugger,
            use_reloader=use_reloader,
            **self.server_options
        )

# Start the Flask server with the given host, port, and settings
manager.add_command("runserver", Server())
        

if __name__ == "__main__":
    import os
    import sys
    
    if sys.argv[1] == "test" or sys.argv[1] == "lint":
        # small hack, to ensure that Flask-Script uses the testing
        # configuration if we are going to run the tests
        os.environ["FLACK_CONFIG"] = "testing"
    manager.run()