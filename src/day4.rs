use std::path::Path;
use anyhow::{anyhow, Result};
use crate::util::get_data;

pub fn day4() -> Result<()> {
  let part1 = day4_part1()?;
  let part2 = day4_part2()?;
  println!("Part 1: {}", "");
  println!("Part 2: {}", "");
  Ok(())
}

#[derive(Debug)]
struct Bingo {
  values: Vec<u32>,
  boards: Vec<Board>,
}

#[derive(Debug)]
struct Board {
  entries: Vec<Vec<Entry>>,
}

#[derive(Debug)]
struct Entry {
  value: u32,
  marked: bool,
}

fn parse_data(data: Vec<String>) -> Result<Bingo> {
  match data.as_slice() {
    [first, rest @ ..] => {
      let boards = parse_boards(rest)?;
      Ok(Bingo {
        values: first.split(',').map(|s| s.parse::<u32>().unwrap()).collect(),
        boards,
      })
    }
    _ => Err(anyhow!("Invalid data")),
  }
}

fn parse_boards(data: &[String]) -> Result<Vec<Board>> {
  let mut current_board: Vec<Vec<u32>> = Vec::new();
  let mut boards = Vec::new();
  for line in data {
    if line.len() == 0 {
      continue;
    } else {
      let values = line.split_whitespace().map(|s| s.parse::<u32>().map_err(|err| anyhow!(err))).into_iter().collect::<Result<Vec<u32>>>()?;
      current_board.push(values);
      if current_board.len() == 5 {
        let board = Board {
          entries: current_board.iter().map(|row| {
            row.iter().map(|&value| Entry {
              value,
              marked: false,
            }).collect()
          }).collect(),
        };
        boards.push(board);
        current_board = Vec::new();
      }
    }
  }
  Ok(boards)
}

fn day4_part1() -> Result<()> {
  let data = get_data(Path::new("./data/day4.txt"))?;
  let bingo = parse_data(data);
  println!("{:?}", bingo);
  Ok(())
}

fn day4_part2() -> Result<()> {
  Ok(())
}
