from speed import Speed

cli = Speed(name="Table Generator")

@cli.main()
def hello(name:str):
    print("Welcome %s !"%name)

@cli.subcommand()
def generate(rows:int,cols:int):
    """
    Generate a table of void cells with | as separator. One cell is 3x3 characters.:
    +---+
    |   |
    +---+
    """
    for i in range(rows):
        print("+"+"---+"*cols)
        print("|"+"   |"*cols)
    print("+"+"---+"*cols)   

@cli.subcommand()
def sum(numbers:list):
    """
    Sum all the numbers in the list
    """
    
    res = 0
    for i in numbers:
        res += int(i)
    print(res)

if __name__ == '__main__':
    cli.run()
