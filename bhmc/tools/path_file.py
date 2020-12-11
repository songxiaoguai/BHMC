import os
def path_absolute():
    return os.path.dirname(os.path.dirname(os.path.abspath("bhmc")))

if __name__ == '__main__':
    print(path_absolute())
