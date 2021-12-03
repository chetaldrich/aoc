use std::env::args;
use std::process;
use anyhow::{anyhow, Result};
use crate::day1::day1;
use crate::day2::day2;
use crate::day3::day3;

mod day1;
mod day2;
mod util;
mod day3;

fn main() -> Result<()> {
  let mut args = args();
  args.next();
  let day = args.next()
    .ok_or(anyhow!("you must provide an integer argument for the day"))?
    .parse::<u32>()?;

  match day {
    1 => day1(),
    2 => day2(),
    3 => day3(),
    _ => {
      println!("You haven't done day {}, try again.", day);
      process::exit(1);
    }
  }
}
