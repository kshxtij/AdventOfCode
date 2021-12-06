use regex::Regex;
use std::cmp;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("../input.txt").unwrap(); // Open the file in read-only mode (ignoring errors).
    let reader = BufReader::new(file);
    let mut p1 = HashMap::<(i32, i32), i32>::new();
    let mut p2 = HashMap::<(i32, i32), i32>::new();

    let re = Regex::new(r"(\d+),(\d+) -> (\d+),(\d+)").unwrap();
    for line in reader.lines() {
        // Read the file line by line using the lines() iterator from std::io::BufRead.
        let line = line.unwrap(); // Ignore errors.
        for cap in re.captures_iter(line.as_str()) {
            let x1 = &cap[1].parse::<i32>().unwrap();
            let y1 = &cap[2].parse::<i32>().unwrap();
            let x2 = &cap[3].parse::<i32>().unwrap();
            let y2 = &cap[4].parse::<i32>().unwrap();
            let dx: i32 = x2 - x1;
            let dy: i32 = y2 - y1;

            for i in 0..1 + cmp::max(dx.abs(), dy.abs()) {
                let x = x1
                    + match dx.cmp(&0) {
                        cmp::Ordering::Less => -1,
                        cmp::Ordering::Equal => 0,
                        cmp::Ordering::Greater => 1,
                    } * i;
                let y = y1
                    + match dy.cmp(&0) {
                        cmp::Ordering::Less => -1,
                        cmp::Ordering::Equal => 0,
                        cmp::Ordering::Greater => 1,
                    } * i;
                if (dx == 0) || (dy == 0) {
                    *p1.entry((x, y)).or_insert(0) += 1;
                }
                *p2.entry((x, y)).or_insert(0) += 1;
            }
        }
    }
    println!(
        "Part 1: {}",
        p1.iter().filter(|&(_, v)| v > &1).count().to_string()
    );
    println!(
        "Part 2: {}",
        p2.iter().filter(|&(_, v)| v > &1).count().to_string()
    );
}