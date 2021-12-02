use std::env::args;
use std::process;
use anyhow::{anyhow, Result};
use crate::day1::day1;
use crate::day2::day2;

mod day1;
mod day2;
mod util;

fn main() -> Result<()> {
  let mut args = args();
  args.next();
  let day = args.next()
    .ok_or(anyhow!("you must provide an integer argument for the day"))?
    .parse::<u32>()?;

  match day {
    1 => day1(),
    2 => day2(),
    _ => {
      println!("You haven't done day {}, try again.", day);
      process::exit(1);
    }
  }
}
