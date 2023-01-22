import sys
from speed.core import Speed, Config

# sys.argv = ['python', 'hello2', '--name=Anthony', '-v', '--hobbies=Basketball,Football,Programming']

def main():
    app = Speed(name="App")

    @app.subcommand(debug=True)
    def hello(v:bool, name:str, hobbies:list):
        pass
    
    @app.subcommand(debug=True)
    def hello2(name:str, age:int):
        pass

    # print(app.config)
    print(app)


if __name__ == '__main__':
    main()