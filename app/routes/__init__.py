from .device_routes import device_bp
from .video_routes import video_bp
from .alarm_routes import alarm_bp
from .index_route import index_bp

__all__ = ['index_bp', 'device_bp', 'video_bp', 'alarm_bp']
