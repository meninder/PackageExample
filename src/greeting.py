
def greet(greeter):
    try:
        print('Hello I am {}'.format(greeter))
        #print('Hello world')

    except Exception as e:
        print('greeting went wrong')

    return None