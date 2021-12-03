use std::path::Path;
use anyhow::{anyhow, Result};
use crate::util::{get_data, lines_from_file};

pub fn day3() -> Result<()> {
  let part1 = day3_part1()?;
  day3_part2()?;
  println!("Part 1: {}", part1);
  Ok(())
}

fn day3_part1() -> Result<usize> {
  let data = get_data(Path::new("./data/day3.txt"))?;

  let mut counts = vec![0; data[0].len()];
  for bin in &data {
    for (i, c) in bin.chars().enumerate() {
      if c == '1' {
        counts[i] += 1;
      }
    }
  }

  let gamma_str = build_str(&counts, data.len() as i32, '1', '0');
  let epsilon_str = build_str(&counts, data.len() as i32, '0', '1');

  let gamma = usize::from_str_radix(&gamma_str, 2).unwrap();
  let epsilon= usize::from_str_radix(&epsilon_str, 2).unwrap();

  Ok(gamma * epsilon)
}

fn build_str(counts: &[i32], size: i32, yes: char, no: char) -> String {
  counts.iter().map(|count| {
    if count < &(size / 2 as i32) {
      yes
    } else {
      no
    }
  }).fold(String::new(), |mut acc, c| {
    acc.push(c);
    acc
  })
}

fn day3_part2() -> Result<()> {
  Ok(())
}
