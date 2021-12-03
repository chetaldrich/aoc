use crate::util::{get_data, lines_from_file};
use anyhow::{anyhow, Result};
use std::path::Path;

pub fn day3() -> Result<()> {
  let part1 = day3_part1()?;
  let part2 = day3_part2()?;
  println!("Part 1: {}", part1);
  println!("Part 2: {}", part2);
  Ok(())
}

fn day3_part1() -> Result<usize> {
  let data = get_data(Path::new("./data/day3.txt"))?;
  let counts = get_counts(&data);

  let gamma_str = build_common_str(&counts, data.len(), '1', '0');
  let epsilon_str = build_common_str(&counts, data.len(), '0', '1');

  let gamma = usize::from_str_radix(&gamma_str, 2).unwrap();
  let epsilon = usize::from_str_radix(&epsilon_str, 2).unwrap();

  Ok(gamma * epsilon)
}

fn get_counts(data: &[String]) -> Vec<usize> {
  let mut counts = vec![0; data[0].len()];
  for bin in data {
    for (i, c) in bin.chars().enumerate() {
      if c == '1' {
        counts[i] += 1;
      }
    }
  }
  counts
}

fn build_common_str(counts: &[usize], size: usize, yes: char, no: char) -> String {
  let half = size as f32 / 2.0;
  counts
    .iter()
    .map(|count| if *count as f32 >= half { yes } else { no })
    .fold(String::new(), |mut acc, c| {
      acc.push(c);
      acc
    })
}

fn day3_part2() -> Result<usize> {
  let data = get_data(Path::new("./data/day3.txt"))?;
  let counts = get_counts(&data);
  let oxygen = find_closest_match(data.clone(), '1', '0');
  let carbon = find_closest_match(data.clone(), '0', '1');
  let i = oxygen.map(|o| o * carbon.unwrap()).unwrap();
  Ok(i)
}

fn find_closest_match(mut data: Vec<String>, yes: char, no: char) -> Result<usize> {
  let mut result = None;
  let mut i = 0;
  while data.len() > 1 {
    let target = build_common_str(&get_counts(&*data), data.len(), yes, no).chars().nth(i).unwrap();
    println!("{:?}, {}, {}", data, target, i);
    data = data
      .into_iter()
      .filter(|s| s.chars().nth(i).unwrap() == target)
      .collect();
    i += 1;
    if data.len() == 1 {
      result = Some(usize::from_str_radix(&data[0], 2).unwrap());
      break;
    }
  }
  result.ok_or(anyhow!("No result found"))
}

mod tests {
  use crate::day3::{build_common_str, find_closest_match, get_counts};

  fn data() -> Vec<String> {
    vec![
      "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
      "00010", "01010",
    ].iter().map(|s| s.to_string()).collect()
  }

  #[test]
  fn test_find_closest_match() {
    let oxygen = find_closest_match(data(), '1', '0');
    assert_eq!(oxygen.unwrap(), 23);
  }

  #[test]
  fn test_counts() {
    let vec = get_counts(&data());
    assert_eq!(vec![7, 5, 8, 7, 5], vec);
  }

  #[test]
  fn test_build_str() {
    let data = data();
    let vec = get_counts(&data);
    assert_eq!("10110", build_common_str(&vec, data.len(), '1', '0'));
  }

  #[test]
  fn test_build_str_2() {
    let data: Vec<String> = vec![
      "11110", "10110", "10111", "10101", "11100", "10000", "11001"
    ].iter().map(|s| s.to_string()).collect();
    let vec = get_counts(&data);
    assert_eq!("10100", build_common_str(&vec, data.len(), '1', '0'));
  }
}
