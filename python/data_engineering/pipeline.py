class Pipeline:
    def __init__(self):
        self.tasks = []

    def task(self):
        def inner(func):
            self.tasks.append(func)
            return func

        return inner


pipeline = Pipeline()


@pipeline.task()
def first_task(x):
    return x ** 2


print(pipeline.tasks)
# pipeline = Pipeline()
# @pipeline.task()
# def first_task(x):
#     return x + 1


@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2


@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4


print(pipeline.run(20))


# USING THE POWER OF DECORATORS
def catch_error(func):
    def inner(*args):
        try:
            return func(*args)

        except Exception as e:
            return e

    return inner


@catch_error
def throws_error():
    raise Exception("Throws Error")


print(throws_error())
