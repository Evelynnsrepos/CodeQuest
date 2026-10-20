interface Point {
  x: number;
  y: number;
}

type Direction = "up" | "down" | "left" | "right";

function move(pos: Point, dir: Direction): Point {
  switch (dir) {
    case "up":
      return { x: pos.x, y: pos.y - 1 };
    case "down":
      return { x: pos.x, y: pos.y + 1 };
    case "left":
      return { x: pos.x - 1, y: pos.y };
    case "right":
      return { x: pos.x + 1, y: pos.y };
  }
}

const start: Point = { x: 0, y: 0 };
console.log(move(start, "up"));
