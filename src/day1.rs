use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
  BufReader::new(File::open(filename)?).lines().collect()
}

fn average_windows(depths: &Vec<i32>) -> Vec<i32> {
  depths
    .windows(3)
    .map(|window| window.iter().sum())
    .collect()
}

fn count_increases(depths: &Vec<i32>) -> i32 {
  let mut increases = 0;
  let mut current_depth = 0;
  for depth in depths {
    if current_depth == 0 {
      current_depth = *depth;
    } else {
      if current_depth < *depth {
        increases += 1;
      }
      current_depth = *depth;
    }
  }
  increases
}

fn get_data() -> Vec<i32> {
  let data = Path::new("./data");
  lines_from_file(data.join("day1.txt"))
    .expect("couldn't get lines")
    .iter()
    .map(|s| s.parse::<i32>().unwrap())
    .collect()
}

pub fn day1_part1() -> i32 {
  count_increases(&get_data())
}

pub fn day1_part2() -> i32 {
  count_increases(&average_windows(&get_data()))
}
