interface Hero {
  name: string;
  hp: number;
  level: number;
}

function levelUp(hero: Hero): Hero {
  return { ...hero, level: hero.level + 1, hp: hero.hp + 10 };
}

const evy = { name: "Evy", hp: 30, level: 1 };
console.log(levelUp(evy));
