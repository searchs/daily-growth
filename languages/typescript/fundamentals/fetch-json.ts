interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

const log = (message: string): void => {
  console.log("INFO:", message);
};

async function fetchTodo(id = 1): Promise<Todo> {
  const response = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`);

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  const todo = (await response.json()) as Todo;

  log(
    `Next todo item: ${todo.id} — ${todo.title} — completed: ${todo.completed}`,
  );

  return todo;
}

void fetchTodo().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error("Unable to fetch todo:", message);
});
