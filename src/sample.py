import argparse

def run(var1, var2):
    var3 = f"{var1}:{var2}"
    print(var3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Input sample argparse args")
    parser.add_argument('--V1', type=int, help='Enter val for var1')
    parser.add_argument('--V2', type=string, help='Enter val for var2')
    args = parser.parse_args()
    run(args.V1, args.V2)
