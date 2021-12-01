use crate::day1::{day1_part1, day1_part2};

mod day1;

fn main() {
  let day1_part1 = day1_part1();
  let day1_part2 = day1_part2();

  println!("day 1 part 1 depth increases: {}", day1_part1);
  println!("day 1 part 2 depth increases: {}", day1_part2);
}
