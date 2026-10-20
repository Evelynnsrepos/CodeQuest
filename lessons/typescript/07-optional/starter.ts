interface Hero {
  name: string;
  hp: number;
}

function hpOf(party: Hero[], name: string): number {
  const hero = party.find((h) => h.name === name);
  return hero.hp;
}

const party: Hero[] = [{ name: "Evy", hp: 30 }, { name: "Mo", hp: 12 }];
console.log(hpOf(party, "Mo"));
console.log(hpOf(party, "Zed"));
