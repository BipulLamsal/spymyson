import os
from app import create_app, config

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', config.PORT))
    # app.run(host = config.HOST, port = config.PORT, debug= config.DEBUG, threaded=True)
    app.run(host = config.HOST, port = port, debug=config.DEBUG, threaded= True)
