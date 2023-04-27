import psutil
from flask import Blueprint, jsonify
from werkzeug.exceptions import InternalServerError


metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics", methods = ["GET"])
def retrive_metrics():
    """Retrives metrics pertaining to syten with respect to processor, ram, disk, network

    Returns:
        dict: sytem metrics 
    """
    data = {}
    # cpu metrics
    cpu_percentage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_frequency = psutil.cpu_freq()
    # memory metrics
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    # disk metrics
    disk_usage = psutil.disk_usage("/")
    # network metrics
    net_io_counters = psutil.net_io_counters()
    
    data["cpu_percentage"] = cpu_percentage
    data["cpu_count"] = cpu_count
    data["cpu_frequency"] = {
        "current": cpu_frequency.current,
        "min": cpu_frequency.min,
        "max": cpu_frequency.max
    }
    data["memory"] = {
        "total": mem.total,
        "available": mem.available,
        "percentage": mem.percent,
        "used": mem.used,
        "free": mem.free,
    }
    
    data['swap'] = {
        "total": swap.total,
        "used": swap.used,
        "free": swap.free,
        "percentage": swap.percent
    }
    
    data["disk_usage"] = {
        "total": disk_usage.total,
        "used": disk_usage.used,
        "free": disk_usage.free,
        "percentage": disk_usage.percent
    }
    
    data["network_io_counters"] = {
        "bytes_sent": net_io_counters.bytes_sent,
        "bytes_recv": net_io_counters.bytes_recv,
        "packets_sent": net_io_counters.packets_sent,
        "packets_recv": net_io_counters.packets_recv,
        "errin": net_io_counters.errin,
        "errout": net_io_counters.errout,
        "dropin": net_io_counters.dropin,
        "dropout": net_io_counters.dropout
    }
    return data