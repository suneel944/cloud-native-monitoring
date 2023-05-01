from flask import Blueprint, render_template, Response

data_stream_bp = Blueprint("event_stream", __name__)

@data_stream_bp.route("/", methods=["GET"])
def make_template():
    # pass the data to the template
    return render_template("index.html")

@data_stream_bp.route("/dashboard-data", methods=["GET"])
def stream_data_to_dashboard():
    def generate():
        import json
        from time import sleep
        from app.blueprints.metrics.Metrics import retrive_metrics
        while True:
            data = retrive_metrics()
            # \n\n is provided to indicate end of sse (server-sent-event)
            yield f"data:{json.dumps(data)}\n\n"
            sleep(3)
    return Response(generate(), mimetype="text/event-stream")
            