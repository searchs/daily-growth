// Consolidated from the historical searchs/domain-driven-js dungeon exercise.
// The original example used an in-memory constructor plus static lookup. This version
// makes the domain invariant explicit and keeps persistence outside the entity.

export class Dungeon {
  private bookedCells = 0;

  constructor(
    readonly id: string,
    readonly capacity: number,
  ) {
    if (capacity <= 0) {
      throw new Error("Dungeon capacity must be positive");
    }
  }

  get availableCells(): number {
    return this.capacity - this.bookedCells;
  }

  bookCells(quantity = 1): void {
    if (!Number.isInteger(quantity) || quantity <= 0) {
      throw new Error("Booking quantity must be a positive integer");
    }

    if (quantity > this.availableCells) {
      throw new Error("Not enough available cells");
    }

    this.bookedCells += quantity;
  }
}

export interface DungeonRepository {
  findById(id: string): Promise<Dungeon | null>;
  save(dungeon: Dungeon): Promise<void>;
}
