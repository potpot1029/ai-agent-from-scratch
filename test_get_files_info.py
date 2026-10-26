from functions.get_files_info import get_files_info


def test_success_root() -> None:
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)


def test_success_sub() -> None:
    result = get_files_info("calculator", "pkg")
    print("Result for pkg directory:")
    print(result)


def test_out_of_working_directory_1() -> None:
    result = get_files_info("calculator", "/bin")
    print("Result for /bin directory:")
    print("  " + result)


def test_out_of_working_directory_2() -> None:
    result = get_files_info("calculator", "../")
    print("Result for ../ directory:")
    print("  " + result)


def test_not_a_directory() -> None:
    result = get_files_info("calculator", "main.py")
    print("Result for main.py:")
    print("  " + result)


if __name__ == "__main__":
    test_success_root()
    test_success_sub()
    test_out_of_working_directory_1()
    test_out_of_working_directory_2()
    test_not_a_directory()
