use std::fs::File;
use std::io::Read;
use std::collections::HashMap;

fn calculate(days: i32)-> usize {
    let mut contents = String::new();
    let _file = File::open("../input.txt")
        .expect("Unable to open")
        .read_to_string(&mut contents);
    let input: Vec<usize> = contents
        .split(',')
        .map(|s| s.parse::<usize>().unwrap())
        .collect();
    let mut fish = HashMap::<usize, usize>::new();
    for s in input.iter() {
        *fish.entry(*s).or_insert(0) += 1
    }
    for _ in 0..days{
        let mut stepped = HashMap::<usize, usize>::new();
        for (value, count) in fish.iter(){
            if value > &0{
                *stepped.entry(value - 1).or_insert(0) += count;
            }
            else{
                *stepped.entry(6).or_insert(0) += count;
                *stepped.entry(8).or_insert(0) += count
            }
        }
        fish = stepped;
    }
    return fish.values().sum::<usize>()
}

fn main() {
    println!("Task 1: {}", calculate(80));
    println!("Task 2: {}", calculate(256));
}
