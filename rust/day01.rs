use std::fs;
use std::i32;
use std::str::FromStr;

fn main () {
    // Read input
    let filename = "../input/01";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the input file");

    let nums:Vec<i32> = contents.split_whitespace()
                        .map(|x| i32::from_str(x).unwrap())
                        .collect();

    // Part 1
    let mut count = 0;
    for i in 1..nums.len() {
        if nums[i] > nums[i-1] {
            count += 1;
        }
    }
    println!("Part 1: {}", count);

    // Part 2
    // Notice how the middle 2 numbers of the overlapping windows cancel out, so we only have to compare the outer edges
    count = 0;
    for i in 3..nums.len() {
        if nums[i] > nums[i-3] {
            count += 1;
        }
    }
    println!("Part 2: {}", count);
}