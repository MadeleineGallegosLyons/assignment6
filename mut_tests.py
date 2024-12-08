import shutil
import subprocess
import random
import sys

def create_mutation_copy(mutation_number):
    source_file = 'target_code.py'
    destination_file = f'target_code_{mutation_number}.py'
    shutil.copy(source_file, destination_file)
    return destination_file
    
def update_test_import(mutation_number):
    test_file = 'test_target_code.py'
    new_import_line = f'from target_code_{mutation_number} import *\n'
        
    with open(test_file, 'r') as file:
        lines = file.readlines()
        
    with open(test_file, 'w') as file:
        for line in lines:
            if line.startswith('from target_code'):
                file.write(new_import_line)
            else:
                file.write(line)


def run_tests(mutation_number):
    test_file = 'test_target_code.py'
    result = subprocess.run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
    print(f'Test results for target_code_{mutation_number}.py:')
    print(result.stdout)
    if result.stderr:
        print('Errors:')
        print(result.stderr)


def mutate_code(mutation_number):
    operators = {
        'logical': ['and', 'or', 'not'],
        'arithmetic': ['+', '-', '*', '/', '%'],
        'relational': ['==', '!=', '>', '<', '>=', '<=', '-=', '+='],
    }

    source_file = f'target_code_{mutation_number}.py'
        
    with open(source_file, 'r') as file:
        code = file.read()
        
    all_operators = [op for ops in operators.values() for op in ops]
    occurrences = [op for op in all_operators if op in code]
        
    if not occurrences:
        print("No operators found to mutate.")
        return
        
    operator_to_mutate = random.choice(occurrences)
    operator_type = next(key for key, value in operators.items() if operator_to_mutate in value)
    new_operator = random.choice([op for op in operators[operator_type] if op != operator_to_mutate])
        
    mutated_code = code.replace(operator_to_mutate, new_operator, 1)
        
    with open(source_file, 'w') as file:
        file.write(mutated_code)
        
    print(f"Mutated {operator_to_mutate} to {new_operator} in {source_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python mut_tests.py <number_of_mutations>")
        sys.exit(1)
            
    try:
        num_mutations = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the number of mutations.")
        sys.exit(1)
            
    for mutation_number in range(1, num_mutations + 1):
        create_mutation_copy(mutation_number)
        update_test_import(mutation_number)
        mutate_code(mutation_number)
        run_tests(mutation_number)

if __name__ == "__main__":
    main()