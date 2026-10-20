function totalGold(bags: number[]): number {
  let total = 0;
  for (const bag of bags) {
    total += bag;
  }
  return total;
}

console.log(totalGold([5, 10, 20]));
