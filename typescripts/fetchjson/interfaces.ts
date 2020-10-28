const logger = (message: string): void => {
  console.log(message);
}

interface Reportable {
  summary(): string;
}

const oldCivic = {
  name: 'Civic',
  year: new Date(),
  broken: true,
  summary(): string {
    return `Name: ${this.name} of year ${this.year}`;
  }
}


const printSummary = (item: Reportable): void => {
  console.log(item.summary());
}

printSummary(oldCivic);
