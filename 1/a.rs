
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    
    let file = File::open("input.txt")?;
    //let file = File::open("example_input.txt")?;
    let reader = io::BufReader::new(file);

    let mut sum:i32 = 0;
    for line in reader.lines() {

        let modified_string = line?.clone()
                                            .replace("one", "one1one")
                                            .replace("two", "two2two")
                                            .replace("three", "three3three")
                                            .replace("four", "four4four")
                                            .replace("five", "five5five")
                                            .replace("six", "six6six")
                                            .replace("seven", "seven7seven")
                                            .replace("eight", "eight8eight")
                                            .replace("nine", "nine9nine");
                
        let numbers: String = modified_string.chars().filter(|c| c.is_digit(10)).collect();
        if let (Some(first),Some(last)) = (numbers.chars().next(), numbers.chars().last()) {

            let concatenated = format!("{}{}", first, last);
            let my_int: i32 = concatenated.parse().unwrap();

            sum = sum + my_int;
        }
    }   
    println!("{:?}", sum);

    Ok(())
}
