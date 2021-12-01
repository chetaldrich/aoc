use std::process;
use crate::day1::{count_increases, lines_from_file};

mod day1;

fn main() {
  let buf = home::home_dir().unwrap_or_else(|| {
    println!("Unable to get home directory on your system");
    process::exit(1);
  });
  let data = buf.as_path().join("other/aoc-2021/data");
  let depths: Vec<i32> = lines_from_file(data.join("day1.txt"))
    .expect("couldn't get lines")
    .iter()
    .map(|s| s.parse::<i32>().unwrap())
    .collect();

  let increases = count_increases(depths);

  println!("depth increases: {}", increases);
}
