fn xp_needed(level: u32) -> u32 {
    level * 100
}

fn main() {
    println!("{}", xp_needed(3));
}
