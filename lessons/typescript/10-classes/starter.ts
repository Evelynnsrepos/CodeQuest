class Inventory {
  private items: string[] = [];

  add(item: string): void {
    this.items.push(item);
  }

  // Write has, remove and count here
}

const bag = new Inventory();
bag.add("potion");
// console.log(bag.has("potion"), bag.count());
