class Vehicle {


  constructor(public color: string) { }

  drive(): void {
    console.log('Not MudBall');
  }

  honk(): void {
    console.log('Vehicle Beep');
  }

}

class Car extends Vehicle {

  constructor(public wheels: number, color: string) {
    super(color);
  }

  drive(): void {
    console.log("Car Voom");
  }

  startDrivingProcess() {
    this.drive();
    this.honk();
  }

}

const vehicle = new Vehicle("blue");
console.log(vehicle.color);
vehicle.honk();


const car = new Car(4, "black");
car.startDrivingProcess();