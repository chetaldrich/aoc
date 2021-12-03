use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};
use std::path::Path;
use anyhow::{anyhow, Result};

pub fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
  BufReader::new(File::open(filename)?).lines().collect()
}

pub fn get_data(location: &Path) -> Result<Vec<String>> {
  Ok(lines_from_file(location)
    .map_err(|err| anyhow!(err))?
    .iter()
    .map(|s| s.to_string())
    .collect())
}
