import csv
from dataclasses import dataclass
from pathlib import Path


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
                    value=int(v[1:]),
                )
            )
    return data


def algo(data: list[DataEntry]) -> int:
    # In part 2, we just have to add the divisor result
    # into total_zeroes.
    # dial has numbers 0-99
    # it takes 100 numbers to rotate 1 full circle
    pos = 50
    total_zeroes = 0

    for d in data:
        print(f"starting {d.direction}{d.value} rotation at {pos}")
        match d.direction:
            case "R":
                if pos != 0:
                    dist_to_zero = 100 - pos
                else:
                    dist_to_zero = 100

                if d.value >= dist_to_zero:
                    hits = 1
                    remaining_dist = d.value - dist_to_zero
                    hits += remaining_dist // 100
                    total_zeroes += hits
                    print(f"  add {hits} hits")

                pos = (pos + d.value) % 100

            case "L":
                if pos != 0:
                    dist_to_zero = pos
                else:
                    dist_to_zero = 100

                if d.value >= dist_to_zero:
                    hits = 1
                    remaining_dist = d.value - dist_to_zero
                    hits += remaining_dist // 100
                    total_zeroes += hits
                    print(f"  add {hits} hits")

                pos = (pos - d.value) % 100

        print(f"  rotated {d.direction}{d.value} to {pos}")

    return total_zeroes


def main():
    cwd = Path(__file__).parent
    # fpath_input = cwd / "sample.txt"
    fpath_input = cwd / "input.txt"
    data = parse_text_file(fpath_input)
    print(f"password is {algo(data)}")


if __name__ == "__main__":
    main()
