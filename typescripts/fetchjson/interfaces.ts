const logger = (message: string): void => {
  console.log(message);
}

interface Vehicle {
  name: string;
  year: number;
  broken: boolean;
}

const oldCivic: Vehicle = {
  name: 'Civic',
  year: 2000,
  broken: true
}


const printVehicle = (vehicle: Vehicle) => {
console.log(`Name: ${vehicle.name}`);
console.log(`Year: ${vehicle.year}`);
console.log(`Broken?:${vehicle.broken}`);

}

printVehicle(oldCivic);
