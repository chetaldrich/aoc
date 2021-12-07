use std::path::Path;
use anyhow::Result;
use crate::util::get_data;

pub fn day5() -> Result<()> {
  let part1 = day5_part1()?;
  let part2 = day5_part2()?;
  println!("Day 5 part 2: {}", part1);
  println!("Day 5 part 2: {}", part2);
  Ok(())
}

struct Line {
  point1: (i32, i32),
  point2: (i32, i32),
}

struct Vents {
  lines: Vec<Line>,
}

fn parse_input() -> Result<Vents> {
  let data = get_data(Path::new("./data/day5.txt"))?;
  Ok(Vents {
    lines: Vec::new(),
  })
}

fn day5_part1() -> Result<u32> {
  Ok(0)
}

fn day5_part2() -> Result<u32> {
  Ok(0)
}