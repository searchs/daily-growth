import axios from 'axios';

const url = 'http://jsonplaceholder.typicode.com/todos/1';
interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

interface Event {
  title: string;
  duration: number;
  anchor: string;
  status: boolean;
}


function createEvent(event: Event) {
logger("generating event for Agenda..");
  return event;
}

axios.get(url).then((response) => {
  console.log(response.data);
  const todo = response.data as Todo;

  const id = todo.id;
  const title = todo.title;
  const completed = todo.completed;

  console.log(`
        Next todo item is with the ID: ${id}
        With the title: ${title}
        Status: ${completed}
  `);
});


const logger = (message: string): void => {
  console.log("INFO:",message);

}


// createEvent
