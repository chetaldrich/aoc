use crate::util::get_data;
use anyhow::{anyhow, Result};
use std::path::Path;

pub fn day5() -> Result<()> {
  let lines = parse_input()?;
  let part1 = day5_part1(&lines)?;
  let part2 = day5_part2(&lines)?;
  println!("Day 5 part 2: {}", part1);
  println!("Day 5 part 2: {}", part2);
  Ok(())
}

#[derive(Debug, Clone)]
struct Line {
  point1: (i32, i32),
  point2: (i32, i32),
}

fn parse_input() -> Result<Vec<Line>> {
  let data = get_data(Path::new("./data/day5.txt"))?;
  let lines = data
    .iter()
    .map(|line| {
      let mut points = line
        .split(" -> ")
        .map(|point| {
          let mut coords = point.split(',').map(|coord| coord.parse::<i32>().unwrap());
          (coords.next().unwrap(), coords.next().unwrap())
        })
        .into_iter()
        .collect::<Vec<(i32, i32)>>();
      points.sort_by_key(|(x, y)| (*x, *y));
      Line {
        point1: points[0],
        point2: points[1],
      }
    })
    .collect::<Vec<Line>>();
  Ok(lines)
}

fn grid(lines: &Vec<Line>) -> Result<Vec<Vec<usize>>> {
  let max_x = lines
    .iter()
    .flat_map(|line| vec![line.point1.0, line.point2.0])
    .max()
    .ok_or(anyhow!("empty list"))?;
  let max_y = lines
    .iter()
    .flat_map(|line| vec![line.point2.1, line.point2.1])
    .max()
    .ok_or(anyhow!("empty list"))?;
  Ok(vec![vec![0; max_x as usize + 1]; max_y as usize + 1])
}

fn mark_horizontal_lines(grid: &mut Vec<Vec<usize>>, lines: &Vec<Line>) {
  let horizontal_lines: Vec<&Line> = lines
    .iter()
    .filter(|line| line.point1.1 == line.point2.1)
    .collect();
  for line in horizontal_lines {
    for x in line.point1.0..=line.point2.0 {
      grid[line.point1.1 as usize][x as usize] += 1;
    }
  }
}

fn mark_vertical_lines(grid: &mut Vec<Vec<usize>>, lines: &Vec<Line>) {
  let vertical_lines: Vec<&Line> = lines
    .iter()
    .filter(|line| line.point1.0 == line.point2.0)
    .collect();
  for line in vertical_lines {
    for y in line.point1.1..=line.point2.1 {
      grid[y as usize][line.point1.0 as usize] += 1;
    }
  }
}

fn mark_diagonal_lines(grid: &mut Vec<Vec<usize>>, lines: &Vec<Line>) {
  let diagonal_lines: Vec<&Line> = lines
    .iter()
    .filter(|line| line.point1.0 != line.point2.0 && line.point1.1 != line.point2.1)
    .collect();
  for line in diagonal_lines {
    let mut x = line.point1.0;
    let mut y = line.point1.1;
    while !(x == line.point2.0 && y == line.point2.1) {
      grid[y as usize][x as usize] += 1;
      if x < line.point2.0 {
        x += 1;
      } else {
        x -= 1;
      }

      if y < line.point2.1 {
        y += 1;
      } else {
        y -= 1;
      }
    }
    grid[y as usize][x as usize] += 1;
  }
}

fn count_overlaps(matrix: &Vec<Vec<usize>>) -> usize {
  matrix
    .iter()
    .map(|row| row.iter().filter(|&&x| x > 1).count())
    .sum()
}

fn day5_part1(lines: &Vec<Line>) -> Result<usize> {
  let mut matrix = grid(lines)?;
  mark_horizontal_lines(&mut matrix, lines);
  mark_vertical_lines(&mut matrix, lines);
  Ok(count_overlaps(&matrix))
}

fn day5_part2(lines: &Vec<Line>) -> Result<usize> {
  let mut matrix = grid(lines)?;
  mark_horizontal_lines(&mut matrix, lines);
  mark_vertical_lines(&mut matrix, lines);
  mark_diagonal_lines(&mut matrix, lines);
  Ok(count_overlaps(&matrix))
}

#[cfg(test)]
mod tests {
  use crate::day5::Line;


  fn lines() -> Vec<Line> {
    let points =vec![
      vec![(0, 9), (5, 9)],
      vec![(8, 0), (0, 8)],
      vec![(9, 4), (3, 4)],
      vec![(2, 2), (2, 1)],
      vec![(7, 0), (7, 4)],
      vec![(6, 4), (2, 0)],
      vec![(0, 9), (2, 9)],
      vec![(3, 4), (1, 4)],
      vec![(0, 0), (8, 8)],
      vec![(5, 5), (8, 2)],
    ];
    let mut lines = Vec::new();
    for mut line in points.into_iter() {
      line.sort_by_key(|(x, y)| (*x, *y));
      lines.push(Line {
        point1: line[0],
        point2: line[1],
      });
    }
    lines
  }

  #[test]
  fn test_day5_part1() {
    let lines = lines();
    assert_eq!(super::day5_part1(&lines).unwrap(), 5);
  }

  #[test]
  fn test_day5_part2() {
    let lines = lines();
    assert_eq!(super::day5_part2(&lines).unwrap(), 12)
  }
}
