import signal

from app import create_app, signal_handler

app = create_app()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == '__main__':
    app.run()