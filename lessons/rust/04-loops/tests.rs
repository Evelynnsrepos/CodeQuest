#[test]
fn three_chests() {
    assert_eq!(total_loot(&[3, 7, 2]), 12, "total_loot(&[3, 7, 2]) should be 12");
}

#[test]
fn no_chests() {
    assert_eq!(total_loot(&[]), 0, "total_loot(&[]) should be 0");
}

#[test]
fn one_big_chest() {
    assert_eq!(total_loot(&[100]), 100, "total_loot(&[100]) should be 100");
}
