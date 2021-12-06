use std::fs;

fn main() {
    let input: Vec<usize> = fs::read_to_string("../input.txt")
        .unwrap()
        .lines()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();
        
    println!(
        "Task 1: {}",
        input
            .windows(2)
            .filter(|x| x[0] < x[1])
            .count()
            .to_string()
    );
    println!(
        "Task 2: {}",
        input
            .windows(3)
            .collect::<Vec<&[usize]>>()
            .windows(2)
            .filter(|x| x[0].iter().sum::<usize>() < x[1].iter().sum::<usize>())
            .count()
            .to_string()
    )
}
