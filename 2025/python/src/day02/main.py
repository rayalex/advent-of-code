from utils.io import read_lines_here

# flatten the "csv" given input is one long line of comma-separated values
# it has only one line
lines = read_lines_here("input.csv", __file__)[0].split(",")  # type: ignore

def part1(data: list[str]) -> int:
    """
    We iteratively check all the numbers in range (inclusive).

    The number is invalid iff:
    - has even length
    - when split in the middle, both parts are the same, e.g.

    99, 1212, 321321

    The output should be the numeric sum of invalid numbers.
    """
    sum = 0
    for r in data:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            # back to string
            iStr = str(i)
            iLen = len(iStr)

            # check if the string is repeated
            if iLen % 2 == 0 and iStr[0:iLen//2] == iStr[-iLen//2:]:
                sum += i

    return sum

def part2(data: list[str]) -> int:
    """
    We iteratively check all the numbers in range (inclusive).

    The number is invalid (per part 2 rules) iff:
    - There are multiple sequences that are repeated, e.g.

    99, 999, 121212 (12 repeated)

    It should be any repeatable sequence and produce the whole number, so:
    121212 - 12 is repeated three times is invalid, but
    121213 - 12 is repeated twice but the number is not made out of the repetitions

    We're solving this by slicing the number and asking if all the slices are the same, e.g.
    We start from the middle and work our way down to 1
    121212 -> 121 212
    121212 -> 12 12 12 (found the match)

    The output should be the numeric sum of invalid numbers.
    """

    def split_by_length(s: str, size: int) -> list[str]:
        if(len(s)) % size != 0:
            return []
        
        return [s[i:i+size] for i in range(0, len(s), size)]

    sum = 0
    for r in data:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            # back to string
            iStr = str(i)
            iLen = len(iStr)

            for split_length in range(iLen // 2, 0, -1):
                splits = split_by_length(iStr, split_length)

                # if we have at least two splits and they are the same, the number is invalid
                # NOTE: len(set(...)) is too slow
                if len(splits) >= 2 and len(set(splits)) == 1:
                    sum += i
                    break # break on first match

    return sum

print("Part 1:", part1(lines))
print("Part 2:", part2(lines))