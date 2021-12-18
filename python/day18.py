#!/usr/bin/env python

from functools import reduce
from itertools import permutations


def reduce_once(line):
    """
    Reduces the given line (a char array), one step: ie, if an element explodes or splits, return True and the new line.
    If no changes were made, returns False and the current line.
    """
    depth = 0
    last_digit_index = -1
    # First see if we need to explode anything
    for i, c in enumerate(line):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        else:
            # assert type(line[i]) == int
            if depth > 4:
                # Explode, assume it's a pair of regular numbers
                # Also assume it's the left-most of the pair
                if last_digit_index >= 0:
                    line[last_digit_index] += line[i]
                for j in range(i + 2, len(line)):
                    if type(line[j]) == int:
                        line[j] += line[i + 1]
                        break
                return True, line[: i - 1] + [0] + line[i + 3 :]
            else:
                last_digit_index = i
    # No explosion; see if we need to split
    for i, c in enumerate(line):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        else:
            # assert type(line[i]) == int
            # assert depth <= 4
            if c > 9:
                return (
                    True,
                    line[:i] + ["[", c // 2, (c + 1) // 2, "]"] + line[i + 1 :],
                )
            else:
                last_digit_index = i
    # No split either; reduction complete
    return False, line


def reduce_full(line):
    modded = True
    while modded:
        modded, line = reduce_once(line)
    return line


def add_fishy(a, b, verbose=False):
    # a = reduce_full(a)
    # b = reduce_full(b)
    c = ["["] + a + b + ["]"]
    result = reduce_full(c)
    if verbose:
        print("  ", tostring_fishy(a))
        print("+ ", tostring_fishy(b))
        print("= ", tostring_fishy(result))
    return result


def parse_fishy(text, do_reduce=True):
    # Assume only single digit numbers occur; splitting on commas will be enough
    lines = [l.strip() for l in text.replace(",", "").split()]
    lines = [[c if c in "[]" else int(c) for c in l] for l in lines]
    if do_reduce:
        lines = [reduce_full(l) for l in lines]
    return lines


def tostring_fishy(line):
    return "".join(str(x) for x in line)


def get_magnitude(line):
    stack = []
    for x in line:
        if x == "[":
            continue
        elif x == "]":
            # Assume line is properly formatted. That means we now have 2 ints on the stack. If we were storing "[",
            # then the 2 ints would be preceded by an "["
            b = stack.pop()
            a = stack.pop()
            stack.append(3 * a + 2 * b)
        else:
            # assert type(x) == int
            stack.append(x)
    # assert len(stack) == 1
    return stack[0]


def run_tests():
    print("\nTest parsing")
    print("================================")
    line = parse_fishy("[[[[[9,8],1],2],3],4]", do_reduce=False)[0]
    assert (
        tostring_fishy(line) == "[[[[[98]1]2]3]4]"
    ), f"Expected: '[[[[[98]1]2]3]4]'; got: {tostring_fishy(line)}"

    def test_reduce_once(testdata, expected):
        print(f"Testing(reduce_once): {testdata} => {expected}")
        lines = parse_fishy(testdata, do_reduce=False)
        result = tostring_fishy(reduce_once(lines[0])[1])
        expected = expected.replace(",", "")
        assert result == expected, f"Expected: '{expected}'; got: '{result}'"

    print("\nTest exploding")
    print("================================")
    test_reduce_once("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]")
    test_reduce_once("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]")
    test_reduce_once("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]")
    test_reduce_once(
        "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    )
    test_reduce_once(
        "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
    )

    def test_addition(testdata, expected):
        print(f"Testing(add_fishy):\n{testdata} => {expected}")
        lines = parse_fishy(testdata)
        result = tostring_fishy(reduce(add_fishy, lines))
        expected = expected.replace(",", "")
        assert result == expected, f"Expected: '{expected}'; got '{result}'"

    print("\nTest addition")
    print("================================")
    test_addition("[1,1]\n[2,2]\n[3,3]\n[4,4]\n", "[[[[1,1],[2,2]],[3,3]],[4,4]]")
    test_addition(
        "[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n", "[[[[3,0],[5,3]],[4,4]],[5,5]]"
    )
    test_addition(
        "[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]\n", "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    )

    def test_magnitude(testdata, expected):
        print(f"Testing(magnitude): {testdata} => {expected}")
        lines = parse_fishy(testdata)
        result = get_magnitude(lines[0])
        assert result == expected, f"Expected: '{expected}'; got '{result}'"

    print("\nTest magnitude")
    print("================================")
    test_magnitude("[[1,2],[[3,4],5]]", 143)
    test_magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384)
    test_magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445)
    test_magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791)
    test_magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137)
    test_magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488)

    print("\nTest full problem, part 1")
    print("================================")
    print("Test 1: file 18.test1")
    with open("../input/18.test1") as f:
        testlines = parse_fishy(f.read())
    result_add = reduce(lambda a, b: add_fishy(a, b, True), testlines)
    assert (
        tostring_fishy(result_add) == "[[[[87][77]][[86][77]]][[[07][66]][87]]]"
    ), f"Expected: '[[[[87][77]][[86][77]]][[[07][66]][87]]]'; got '{tostring_fishy(result_add)}'"
    result = get_magnitude(result_add)
    assert result == 3488, f"Expected 3488; got {result}"

    print("Test 2: file 18.test2")
    with open("../input/18.test2") as f:
        testlines = parse_fishy(f.read())
    result_add = reduce(add_fishy, testlines)
    assert (
        tostring_fishy(result_add) == "[[[[66][76]][[77][70]]][[[77][77]][[78][99]]]]"
    ), f"Expected: '[[[[66][76]][[77][70]]][[[77][77]][[78][99]]]]'; got '{tostring_fishy(result_add)}'"
    result = get_magnitude(result_add)
    assert result == 4140, f"Expected 4140; got {result}"

    print("\nTest part 2: largest sum of any two lines")
    print("================================")
    print("Test: file 18.test2")
    with open("../input/18.test2") as f:
        testlines = parse_fishy(f.read())
    test_sum = -1
    for a, b in permutations(testlines, 2):
        test_sum = max(test_sum, get_magnitude(add_fishy(a, b)))
    assert test_sum == 3993, f"Expected 3993; got {test_sum}"


with open("../input/18") as f:
    lines = parse_fishy(f.read())

p1 = get_magnitude(reduce(add_fishy, lines))
print(f"Part 1: {p1}")


with open("../input/18") as f:
    lines = parse_fishy(f.read())

max_sum = -1
for a, b in permutations(lines, 2):
    max_sum = max(max_sum, get_magnitude(add_fishy(a, b)))
print(f"Part 2: {max_sum}")

# run_tests()
