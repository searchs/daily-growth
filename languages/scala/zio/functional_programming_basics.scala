package learning.zio

/**
  * Functional-programming foundations originally explored while learning ZIO.
  *
  * The examples contrast partial vs total functions, deterministic state passing,
  * mutation and side effects.
  */
object FunctionalProgrammingBasics extends App {

  def simpleDivide(a: Int, b: Int): Int = a / b

  def divideTotal(a: Int, b: Int): Option[Int] =
    if (b != 0) Some(a / b) else None

  final case class RNG(seed: Long) {
    def nextInt: (Int, RNG) = {
      val newSeed = (seed * 0x5DEECE66DL + 0xBL) & 0xFFFFFFFFFFFFL
      val nextRng = RNG(newSeed)
      val value = (newSeed >>> 16).toInt
      (value, nextRng)
    }
  }

  def generateRandomInt(rng: RNG): (Int, RNG) = rng.nextInt

  val initial = RNG(10)
  val (first, rng1) = generateRandomInt(initial)
  val (second, _) = generateRandomInt(rng1)

  assert(divideTotal(5, 0).isEmpty)
  assert(divideTotal(4, 2).contains(2))
  assert(first != second)

  // Examples such as println, mutable vars, external API calls and database
  // access are intentionally treated as effects rather than pure domain logic.
}
