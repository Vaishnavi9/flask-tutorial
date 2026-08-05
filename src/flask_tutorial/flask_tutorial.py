from flask import Flask

my_app = Flask("My first Application")


@my_app.route("/")
def hello_world():
    return "Hello World!"


def main():
    my_app.run(debug=True)


if __name__ == "__main__":
    main()
