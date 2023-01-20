from speed.core import Speed, Config


def main():
    config = Config()
    app = Speed(name="App", config=config)

    @app.transform(required=True, short_name=True)
    def comp(cities:list = ["1","2","3"],name:str="Anthony", age:int=16):
        print(cities, name, age)

    d = lambda h: {k:v[1] for (k,v) in h.items()}
    conf = d(app.config)
    for i in app.config:
        i(**conf[i])

if __name__ == '__main__':
    main()