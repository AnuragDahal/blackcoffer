from core import create_app
import os

app = create_app()

if __name__ == "__main__":
    # os.environ["FLASK_ENV"] = "development"
    # app.run(host='127.0.0.1', port=5000
    #         )

    os.environ["FLASK_ENV"] = "production"
    app.run(host='0.0.0.0', port=5000)
