from pathlib import Path
import sys

def read_lines_from_stdin() -> list[str]:
    return [line.rstrip("\n") for line in sys.stdin]

def read_lines_relative(name: str) -> list[str]:
    return Path(__file__).with_name(name).read_text().splitlines()

def read_lines_here(filename: str, here: str) -> list[str]:
    return (Path(here).with_name(filename)).read_text().splitlines()

def read_csv_lines_here(filename: str, here: str) -> list[list[str]]:
    return [line.split(",") for line in read_lines_here(filename, here)]