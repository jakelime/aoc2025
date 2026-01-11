import csv
from pathlib import Path
from dataclasses import dataclass

PT_START = 50
PT_MAX = 99
PT_MIN = 0


@dataclass
class DataEntry:
    direction: str
    value: int


def parse_text_file(fpath: Path) -> list[DataEntry]:
    data = []
    with open(fpath, "r", newline="\n") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            v = row[0]
            data.append(
                DataEntry(
                    direction=v[0],
                    value=int(v[1:]) % (PT_MAX + 1),
                )
            )
    return data


def algo(data: list[DataEntry]) -> int:
    result = PT_START
    count_of_zero = 0
    for d in data:
        match d.direction:
            case "L":
                result -= d.value
                if result < PT_MIN:
                    result = PT_MAX + result + 1
            case "R":
                result += d.value
                if result > PT_MAX:
                    result = result - (PT_MAX + 1)
        if result == 0:
            count_of_zero += 1

        print(f"rotated {d.direction}{d.value} to {result}")

    print(f"{count_of_zero=}")
    return count_of_zero


def main():
    cwd = Path(__file__).parent
    fpath_input = cwd / "input.txt"
    data = parse_text_file(fpath_input)
    algo(data)


if __name__ == "__main__":
    main()
