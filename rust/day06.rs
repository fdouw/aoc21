use std::fs;
use std::str::FromStr;

fn fishcount(initial: &Vec<i32>, days: i32) -> i64 {
    // Returns the total number of fish after <days> days, given an initial population <initial>.
    let mut fishcounts: [i64; 9] = [0; 9];
    for f in initial {
        fishcounts[*f as usize] += 1;
    }
    for _d in 0..days {
        let spawncount = fishcounts[0];
        for i in 1usize..9 {
            fishcounts[i - 1] = fishcounts[i];
        }
        fishcounts[8] = spawncount;
        fishcounts[6] += spawncount;
    }
    return fishcounts.iter().sum();
}

fn main() {
    let filename = "../input/06";
    let contents = fs::read_to_string(filename).expect("Reading input file failed!");
    let fish = contents
        .trim()
        .split(",")
        .map(|f| i32::from_str(&f).unwrap())
        .collect();

    let part1 = fishcount(&fish, 80);
    let part2 = fishcount(&fish, 256);
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
