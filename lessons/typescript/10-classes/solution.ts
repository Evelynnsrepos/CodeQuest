class Inventory {
  private items: string[] = [];

  add(item: string): void {
    this.items.push(item);
  }

  has(item: string): boolean {
    return this.items.includes(item);
  }

  remove(item: string): boolean {
    const index = this.items.indexOf(item);
    if (index === -1) {
      return false;
    }
    this.items.splice(index, 1);
    return true;
  }

  count(): number {
    return this.items.length;
  }
}

const bag = new Inventory();
bag.add("potion");
console.log(bag.has("potion"), bag.count());
