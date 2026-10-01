let age: number = 30;
let complete: boolean;

let nothingMuch: null = null;

let colors: string[] = ['red', 'green', 'blue'];

colors.forEach((c) => {
  console.log(c);
});


const json = '{"x": 10, "y": 15}';
// const coordinates = JSON.parse(json);
const coordinates: { x: number; y: number } = JSON.parse(json);

console.log(coordinates);




class Car { }

let car: Car = new Car();

//object literal
let point: { x: number; y: number } = {
  x: 10,
  y: 20,
};

const logNumber: (i: number) => void = (i: number) => {
  console.log(i);
};

//Function that returns the 'any' type

const add = (a: number, b: number): number => {
  return a + b
}


const logger = (message: string): void => {
  console.log(message);
}

const todaysWeather = {
  date: new Date(),
  weather: 'sunny'
};

const logWeather = (forecast: { date: Date, weather: string }) => {
  console.log("\nlogWeather Reporting Module\n")
  console.log(forecast.date);
  console.log(forecast.weather);
};


logWeather(todaysWeather);

const logSunny = ({ date, weather }: { date: Date, weather: string }): void => {
  console.log("\nLogSunny Weather Reports\n ")
  console.log(date);
  console.log(weather);
}


logSunny(todaysWeather);