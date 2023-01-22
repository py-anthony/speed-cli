import sys
from speed.core import Speed, Config

def main():
    app = Speed(name="App")

    @app.transform()
    def hello(v:bool, name:str, hobbies:list):
        pass

    # print(app.config)
    print(app.uconfig)


if __name__ == '__main__':
    main()