fn total_loot(chests: &[u32]) -> u32 {
    let mut total = 0;
    for gold in chests {
        total += *gold;
    }
    total
}

fn main() {
    println!("{}", total_loot(&[3, 7, 2]));
}
