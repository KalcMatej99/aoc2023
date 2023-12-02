
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    
    let file = File::open("input.txt")?;
    //let file = File::open("example_input.txt")?;
    let reader = io::BufReader::new(file);

    let mut sum:i32 = 0;
    let mut sum_p:i32 = 0;
    for line in reader.lines() {
        let line = line?;

        let mut is_valid: bool = true;

        let line_clone = line.clone();
        let mut parts = line_clone.split(":");

        let mut game_id = 0;
        let mut cubes = "";

        match parts.next() {
            Some(val) => {


                let last_char: String = val.chars().filter(|c| c.is_digit(10)).collect();

                match last_char.parse::<i32>() {
                    Ok(num) => {
                        game_id = num;
                    }
                    Err(err) => {
                        println!("Failed to parse: {}", err);
                    }
                }
            }
            None => {
                println!("No first element found");
            }
        }

        match parts.last() {
            Some(val) => {
                cubes = val.trim();
            }
            None => {
                println!("No last element found");
            }
        }

        print!("{} ", game_id);
        print!("{} ", cubes);


        let shows = cubes.split(";");

        let mut red:i32 = 0;
        let mut green:i32 = 0;
        let mut blue:i32 = 0;

        for show in shows {

            let showed_cubes = show.split(",");
            

            for showed_cube_color in showed_cubes {

                let n_str:String = showed_cube_color.chars().filter(|c| c.is_digit(10)).collect();

                match n_str.parse::<i32>() {
                    Ok(n) => {
                        if showed_cube_color.contains("red") {
                            red = red.max(n);
                        }
                        if showed_cube_color.contains("green") {
                            green = green.max(n);
                        }
                        if showed_cube_color.contains("blue") {
                            blue = blue.max(n);
                        }
                    }
                    Err(err) => {
                        println!("Failed to parse: {}", err);
                    }
                }
            }

            
        }

        if red >= 13 || green >= 14 || blue >= 15 {
            is_valid = false;
        }

        let product:i32 = red * green * blue;

        println!("{}", is_valid);
        

        if is_valid {
            sum = sum + game_id;
        }

        sum_p = sum_p + product;
    }   
    println!("{:?}", sum);
    println!("{:?}", sum_p);

    Ok(())
}
