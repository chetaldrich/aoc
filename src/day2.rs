use std::path::Path;
use anyhow::{anyhow, Result};
use crate::util::{get_data, lines_from_file};

pub fn day2() -> Result<()> {
  day2_part1()?;
  day2_part2()?;
  Ok(())
}

fn day2_part1() -> Result<()> {
  let mut horizontal = 0;
  let mut vertical = 0;
  let data = get_data(Path::new("./data/day2.txt"))?;
  for line in data {
    let values = line.split(' ').collect::<Vec<&str>>();
    let movement= match values.as_slice() {
      [command, value] => (command, value.parse::<i32>()?),
      _ => panic!("Invalid line: {:?}", line)
    };

    match *movement.0 {
      "forward" => horizontal += movement.1,
      "down" => vertical += movement.1,
      "up" => vertical -= movement.1,
      _ => panic!("Invalid command: {:?}", movement.0)
    }
  }
  println!("day 2 part 1: {}", horizontal * vertical);
  Ok(())
}

fn day2_part2() -> Result<()> {
  let mut aim = 0;
  let mut horizontal = 0;
  let mut depth = 0;

  let data = get_data(Path::new("./data/day2.txt"))?;
  for line in data {
    let values = line.split(' ').collect::<Vec<&str>>();
    let movement= match values.as_slice() {
      [command, value] => (*command, value.parse::<i32>()?),
      _ => panic!("Invalid line: {:?}", line)
    };

    match movement.0 {
      "forward" => {
        horizontal += movement.1;
        depth += movement.1 * aim;
      },
      "down" => aim += movement.1,
      "up" => aim -= movement.1,
      _ => panic!("Invalid command: {:?}", movement.0)
    }
  }

  println!("day 2 part 2: {}", horizontal * depth);
  Ok(())
}
