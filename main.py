from speed.core import Speed, Config

def main():
    config = Config()
    app = Speed(name="App", config=config)

    @app.transform()
    def hello(name: str, hobbies: list, is_student: bool, age: int):
        pass

    print(app.config)


if __name__ == '__main__':
    main()