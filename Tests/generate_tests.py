import os
import shutil
import argparse
import input_generate
import ocean

def main(test_count, line_count):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "files", "outputs")
    input_path = os.path.join(script_dir, "files", "inputs")

    os.makedirs(output_path, exist_ok=True)
    os.makedirs(input_path, exist_ok=True)

    digits = len(str(test_count))
    for i in range(1, test_count + 1):
        input_file = os.path.join(input_path, f"input{i:0{digits}d}.txt")
        output_file = os.path.join(output_path, f"output{i:0{digits}d}.txt")
        if i != 1:
            with open(input_file, "w") as f:
                f.write(input_generate.generate(line_count))
        else:
            source_file = "randtest0.in"  # The file you want to copy
            with open(source_file, "r") as src, open(input_file, "w") as dst:
                shutil.copyfileobj(src, dst)
        ocean.main(input_file, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test files and run ocean.main")
    parser.add_argument("test_count", type=int, help="Number of tests to generate")
    parser.add_argument("line_count", type=int, help="Number of lines per test file")

    args = parser.parse_args()
    main(args.test_count, args.line_count)
