function describeReward(reward: number | string): string {
  if (typeof reward === "number") {
    return `${reward} gold`;
  }
  return `Item: ${reward}`;
}

console.log(describeReward(50));
console.log(describeReward("Fire Sword"));
