function damage(attack: number, defense: number): number {
  return Math.max(0, attack - defense);
}

console.log(damage(10, 3));
