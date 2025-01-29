import atexit

from app import create_app, signal_handler, save_status
import signal

app = create_app()
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

atexit.register(save_status)

if __name__ == '__main__':
    app.run()