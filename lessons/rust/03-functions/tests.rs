#[test]
fn level_1_needs_100() {
    assert_eq!(xp_needed(1), 100, "xp_needed(1) should be 100");
}

#[test]
fn level_5_needs_500() {
    assert_eq!(xp_needed(5), 500, "xp_needed(5) should be 500");
}

#[test]
fn level_0_needs_0() {
    assert_eq!(xp_needed(0), 0, "xp_needed(0) should be 0");
}
