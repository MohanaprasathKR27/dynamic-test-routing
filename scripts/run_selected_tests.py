import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from test_selector import select_tests


def main():
    if len(sys.argv) < 2:
        print("Provide changed file paths.")
        return

    changed_files = sys.argv[1:]
    selected_tests = select_tests(changed_files)

    if not selected_tests:
        print("No matching tests found.")
        return

    print("Selected tests:")
    for test in selected_tests:
        print(test)

    print("\nRunning selected tests...")
    subprocess.run(
        [sys.executable, "-m", "pytest", "-v"] + selected_tests,
        cwd=ROOT
    )


if __name__ == "__main__":
    main()