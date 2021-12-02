
use std::fs;
use std::i32;
use std::str::FromStr;

fn main () {
    // Read input
    let filename = "../input/02";
    let contents = fs::read_to_string(filename).expect("Reading input file failed");

    // Part 1
    // compute movements, they are commutative
    let forward:i32 = contents.lines()
                              .filter(|l| l.starts_with("forward"))
                              .map(|l| i32::from_str(&l[8..]).unwrap())
                              .sum();
    let up:i32 = contents.lines()
                         .filter(|l| l.starts_with("up"))
                         .map(|l| i32::from_str(&l[3..]).unwrap())
                         .sum();
    let down:i32 = contents.lines()
                           .filter(|l| l.starts_with("down"))
                           .map(|l| i32::from_str(&l[5..]).unwrap())
                           .sum();
    println!("Part 1: {}", forward * (down - up));

    // Part 2
    // Use the fact that forward is the same as in part 1
    let mut aim = 0;
    let mut depth = 0;
    for line in contents.lines() {
        if line.starts_with("up") {
            aim -= i32::from_str(&line[3..]).unwrap();
        }
        else if line.starts_with("down") {
            aim += i32::from_str(&line[5..]).unwrap();
        }
        else {  // line.starts_with("forward")
            depth += aim * i32::from_str(&line[8..]).unwrap();
        }
    }
    println!("Part 2: {}", forward * depth);
}