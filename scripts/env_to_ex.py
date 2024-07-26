import os
import argparse

files_to_convert = [".env", ".env.local", ".env.development", ".env.test", ".env.production"]

def find_and_create_example_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename in files_to_convert:
                env_path = os.path.join(dirpath, filename)
                example_path = os.path.join(dirpath, filename + ".example")

                with open(env_path, 'r') as env_file:
                    lines = env_file.readlines()

                with open(example_path, 'w') as example_file:
                    key = None
                    for line in lines:
                        if line.startswith('#'):
                            example_file.write(line)
                        elif '=' in line:
                            key = line.split('=')[0].strip()
                            example_file.write(f'{key}=\n')
                        elif key:
                            # This is a continuation of a multi-line value, so just write a newline
                            example_file.write('\n')
                        else:
                            example_file.write(line)

                print(f'Created {example_path} from {env_path}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find .env files and create .env.example files with only keys.")
    parser.add_argument('root_dir', type=str, help='The root directory to search for .env files')
    args = parser.parse_args()

    find_and_create_example_files(args.root_dir)