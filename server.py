from app import create_app, config
app = create_app()

if __name__ == '__main__':
    # app.run(host = config.HOST, port = config.PORT, debug= config.DEBUG, threaded=True)
    app.run(host = config.HOST, debug=config.DEBUG, threaded= True)
