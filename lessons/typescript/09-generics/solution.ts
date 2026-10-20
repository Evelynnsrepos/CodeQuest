function firstOr<T>(items: T[], fallback: T): T {
  return items.length > 0 ? items[0] : fallback;
}

console.log(firstOr([3, 9], 0));
console.log(firstOr<string>([], "none"));
