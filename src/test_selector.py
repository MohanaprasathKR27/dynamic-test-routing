import subprocess
from pathlib import Path

TEST_MAP = {
    "pricing.py": ["tests/test_pricing.py"],
    "cart.py": ["tests/test_cart.py"],
    "inventory.py": ["tests/test_inventory.py"],
}


def get_changed_files():
    changed = set()

    commands = [
        ["git", "diff", "--name-only", "HEAD"],
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
    ]

    for command in commands:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            changed.update(result.stdout.splitlines())

    return sorted(changed)


def select_tests(changed_files):
    selected = set()

    for file in changed_files:
        filename = Path(file).name

        if filename in TEST_MAP:
            selected.update(TEST_MAP[filename])

    return sorted(selected)