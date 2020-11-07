from horecapp import app


app.logger.info("Running app in wsgi...")
if __name__ == "__main__":
    app.run()
