
from functions.get_file_content import get_file_content


def test_truncate() -> None:
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

def test_success() -> None:
    result = get_file_content("calculator", "main.py")
    print("Result for main.py:")
    print(result)

def test_success_sub() -> None:
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py:")
    print(result)


def test_out_of_working_directory() -> None:
    result = get_file_content("calculator", "/bin/cat")
    print("Result for /bin/cat:")
    print("  " + result)


def test_file_not_exist() -> None:
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for pkg/does_not_exist.py:")
    print("  " + result)


def test_not_a_file() -> None:
    result = get_file_content("calculator", "pkg")
    print("Result for pkg:")
    print("  " + result)


if __name__ == "__main__":
    test_truncate()
    test_success()
    test_success_sub()
    test_out_of_working_directory()
    test_file_not_exist()
    test_not_a_file()