import inspect

def get_function_location(func):
    source_lines, _ = inspect.getsourcelines(func)
    return inspect.getsourcefile(func), source_lines

# Kullanım örneği
def example_function():
    print("Hello, World!")

file_path, source_code = get_function_location(example_function)
print("Dosya Yolu:", file_path)
print("Kaynak Kodu:")
for line in source_code:
    print(line.strip())
