
from functions.run_python_file import run_python_file 


def test_main() -> None:
    result = run_python_file("calculator", "main.py")
    print("Result for main.py:")
    print(result)

def test_main_with_args() -> None:
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for main.py (3 + 5):")
    print(result)
    
def test_tests() -> None:
    result = run_python_file("calculator", "tests.py")
    print("Result for tests.py:")
    print(result)
    
def test_out_of_working_directory() -> None:
    result = run_python_file("calculator", "../main.py")
    print("Result for ../main.py:")
    print(result)

def test_not_exist_file() -> None:
    result = run_python_file("calculator", "nonexistent.py")
    print("Result for nonexistent.py:")
    print(result)
    
def test_non_py_file() -> None:
    result = run_python_file("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    print(result)
    
if __name__ == "__main__":
    test_main()
    test_main_with_args()
    test_tests()
    test_out_of_working_directory()
    test_not_exist_file()
    test_non_py_file()