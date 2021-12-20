#!/usr/bin/env python


def print_image(image):
    for line in image:
        print("".join(line.replace("0", ".").replace("1", "#")))


def enhance_pixel(x, y, image, algo):
    idx = int(
        image[y - 1][x - 1 : x + 2]
        + image[y][x - 1 : x + 2]
        + image[y + 1][x - 1 : x + 2],
        2,
    )
    return algo[idx]


iterations = 50
safety_margin = 50
margin = 2 * iterations + safety_margin

with open("../input/20") as f:
    rawdata = f.read().replace(".", "0").replace("#", "1").splitlines()
    algo = rawdata[0]
    image = ["0" * margin + l + "0" * margin for l in rawdata[2:]]
    h_edge = "0" * len(image[0])
    image = [h_edge] * margin + image + [h_edge] * margin

for i in range(iterations):
    new_image = [h_edge]
    for y in range(1, len(image) - 1):
        # The "0" at the boundaries will cause issues, because they should flip
        new_image.append(
            "0"
            + "".join(
                enhance_pixel(x, y, image, algo) for x in range(1, len(h_edge) - 1)
            )
            + "0"
        )
        pass
    image = new_image + [h_edge]

# To account for boundary issues, cut off the outer pixels
pixel_count = sum(
    1 if image[y][x] == "1" else 0
    for y in range(safety_margin, len(image) - safety_margin)
    for x in range(safety_margin, len(image[y]) - safety_margin)
)
print(f"Part 1: {pixel_count}")


def test():
    #   # . . # .
    #   #[. . .].
    #   #[# . .]#
    #   .[. # .].
    #   . . # # #
    test_image = ["10010", "10000", "11001", "00100", "00111"]
    test_algo = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##".replace(
        ".", "0"
    ).replace(
        "#", "1"
    )
    assert enhance_pixel(2, 2, test_image, test_algo) == "1"


test()
