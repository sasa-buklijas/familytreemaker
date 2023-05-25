import os
import sys
from pathlib import Path

generated_file: str = 'generated.txt'
input_dir: str= 'input'

# input test files are called i_n.txt
    # where n is number of test
if len(sys.argv) == 1:  # run all tests
    input_files = sorted([i for i in Path.cwd().glob(f'{input_dir}{os.sep}i_*.txt')])
else:
    input_files: list = []
    for i in sys.argv[1:]:
        _ = f'i_{i}.txt'
        input_files.append(_)

for input_file in input_files:
    #input_file = input_file.name    # get just filename and convert to str
    print(f'TestCase: {input_file}')

    # expected output files are called o_n.txt
    expected_file = f'expected_output{os.sep}o' + input_file[1:]

    # generate output file
    os.system(f'python ..{os.sep}familytreemaker.py \
                {input_dir}{os.sep}{input_file} > {generated_file}')

    # check for differences between generated and expected output
    rv = os.system(f'diff {generated_file} {expected_file} >/dev/null')
    if rv == 0:
        print('    OK\n')
    else:
        print(f'    PROBLEM with TestCase: {input_file} !!!')
        os.system(f'sdiff {generated_file} {expected_file}')
        print()     # just for new line
