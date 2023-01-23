import sys
from speed.core import Speed, Config

# sys.argv = ['python', 'hello2', '--name=Anthony', '-v', '--hobbies=Basketball,Football,Programming']

def main():
    app = Speed(name="App")

    @app.subcommand(debug=False)
    def hello(v:bool, name:str, hobbies:list):
        if v:
            print(f"Hello {name}, your hobbies are {hobbies}, I'm glad to meet you!")
        else:
            print(f"Hello {name}!")

    @app.subcommand(debug=False)
    def hello2(message:bool):
        if message:
            print("You activate the message flag")
        else:
            print("You didn't activate the message flag")

    # print(app.config)
    app.run()


if __name__ == '__main__':
    main()