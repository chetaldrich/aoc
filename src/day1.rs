use std::path::Path;
use anyhow::{anyhow, Result};
use crate::util::lines_from_file;

fn average_windows(depths: &[i32]) -> Vec<i32> {
  depths
    .windows(3)
    .map(|window| window.iter().sum())
    .collect()
}

fn count_increases(depths: &[i32]) -> i32 {
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

fn get_data() -> Result<Vec<i32>> {
  let data = Path::new("./data");
  lines_from_file(data.join("day1.txt"))?
    .iter()
    .map(|s| s.parse::<i32>().map_err(|err| anyhow!(err)))
    .collect()
}

fn day1_part1() -> Result<i32> {
  Ok(count_increases(&get_data()?))
}

fn day1_part2() -> Result<i32> {
  Ok(count_increases(&average_windows(&get_data()?)))
}

pub fn day1() -> Result<()> {
  let day1_part1 = day1_part1()?;
  let day1_part2 = day1_part2()?;

  println!("day 1 part 1 depth increases: {}", day1_part1);
  println!("day 1 part 2 depth increases: {}", day1_part2);
  Ok(())
}
