import time
from dotenv import load_dotenv
from Engine import Engine

def main():
    myEngine = Engine(mode="cli")
    myEngine.run()
    myEngine.destroy()


if __name__ == "__main__":
    load_dotenv()
    start_time = time.time()
    main()
    print("Python execution time: %.6f seconds" % (time.time() - start_time))