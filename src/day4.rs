use std::path::Path;
use anyhow::{anyhow, Result};
use crate::util::get_data;

pub fn day4() -> Result<()> {
  let part1 = day4_part1()?;
  let _part2 = day4_part2()?;
  println!("Part 1: {}", part1);
  println!("Part 2: ");
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

#[derive(Debug, Copy, Clone)]
struct Entry {
  value: u32,
  marked: bool,
}

fn parse_data(data: Vec<String>) -> Result<Bingo> {
  match data.as_slice() {
    [first, rest @ ..] => {
      let boards = parse_boards(rest)?;
      let values = first.split(',').map(|s| s.parse::<u32>().map_err(|err| anyhow!(err))).collect::<Result<Vec<u32>>>()?;
      Ok(Bingo {
        values,
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
    if line.is_empty() {
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

fn mark_board(board: &mut Board, value: u32) {
  for row in board.entries.iter_mut() {
    for entry in row.iter_mut() {
      if entry.value == value {
        entry.marked = true;
      }
    }
  }
}

fn check_bingo(board: &Board) -> bool {
  for row in board.entries.iter() {
    if row.iter().all(|entry| entry.marked) {
      return true;
    }
  }

  for i in 0..board.entries.len() {
    let mut marked_values = Vec::new();
    for j in 0..board.entries.len() {
      marked_values.push(board.entries[j][i].marked);
    }
    if marked_values.iter().all(|&value| value) {
      return true;
    }
  }

  false
}

fn score(board: &Board) -> u32 {
  let mut score = 0;
  for row in board.entries.iter() {
    for entry in row.iter() {
      if !entry.marked {
        score += entry.value;
      }
    }
  }
  score
}

fn day4_part1() -> Result<u32> {
  let data = get_data(Path::new("./data/day4.txt"))?;
  let mut bingo = parse_data(data)?;

  for value in bingo.values.iter() {
    for board in &mut bingo.boards {
      mark_board(board, *value);
      if check_bingo(board) {
        return Ok(score(board) * value);
      }
    }
  }

  Err(anyhow!("No bingo found"))
}

fn day4_part2() -> Result<()> {
  Ok(())
}
