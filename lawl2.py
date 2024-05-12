import itertools

def generate_alphanumeric_combinations():
    alphanumeric_chars = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return itertools.product(alphanumeric_chars, repeat=2)

def write_to_file(combinations):
    with open('alphanumericCombs.txt', 'w') as file:
        for comb in combinations:
            file.write(''.join(comb) + '\n')

if __name__ == "__main__":
    combinations = generate_alphanumeric_combinations()
    write_to_file(combinations)
    print("Alphanumeric combinations written to alphanumericCombs.txt")