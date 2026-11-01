import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from selector import select_tests, get_changed_files

def main():
    changed_files = get_changed_files()

    print("Changed files:", changed_files)

    selected_tests = select_tests(changed_files)

    if not selected_tests:
        print("No matching tests found.")
        return

    print("Selected tests:", selected_tests)

    subprocess.run(
        [sys.executable, "-m", "pytest", "-v"] + selected_tests,
        cwd=ROOT
    )


if __name__ == "__main__":
    main()