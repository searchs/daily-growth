# Scala Functional Programming Notes

This section consolidates small Scala exercises from the retired `underscore-scala` repository.

## Durable ideas preserved

- immutable state with case classes and `copy`
- overloaded methods that return new values instead of mutating existing instances
- companion-object constructors (`apply`)
- composition of small domain operations
- algebraic modelling through case classes and traits

The original repository also contained many tiny tutorial objects and package experiments. Those are intentionally not reproduced here; the goal is to retain the reusable concepts in a compact form.

## Example: immutable counter

```scala
final case class Counter(count: Int = 0) {
  def increment: Counter = copy(count = count + 1)
  def decrement: Counter = copy(count = count - 1)
  def incrementBy(value: Int): Counter = copy(count = count + value)
  def decrementBy(value: Int): Counter = copy(count = count - value)
}
```

## Example: companion constructor

```scala
final case class Timestamp(seconds: Long)

object Timestamp {
  def fromHms(hours: Int, minutes: Int, seconds: Int): Timestamp =
    Timestamp(hours.toLong * 3600 + minutes.toLong * 60 + seconds)
}
```

These examples retain the core learning from `underscore-scala` while using clearer names and modern, import-safe code.
