use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, Read};
use std::path::Path;

pub fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
  BufReader::new(File::open(filename)?).lines().collect()
}

pub fn count_increases(depths: Vec<i32>) -> i32 {
  let mut increases = 0;
  let mut current_depth = 0;
  for depth in depths {
    if current_depth == 0 {
      current_depth = depth;
    } else {
      if current_depth < depth {
        increases += 1;
      }
      current_depth = depth;
    }
  }
  increases
}
