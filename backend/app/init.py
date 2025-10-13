try:
    from .main import app
except ImportError:  # fallback when imported as plain module
    from main import app

__all__ = ['app']