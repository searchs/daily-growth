const profile = {
  name: 'alex',
  age: 20,
  coords: {
    lat: 10,
    lng: 15
  },
  setAge(age: number): void {
    this.age = age;
  }
};


const { age }: { age: number } = profile;

const { coords: { lat, lng } }: { coords: { lat: number, lng: number } } = profile;

profile.setAge(42);
console.log(profile.age);



