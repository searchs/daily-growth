object TuplesSamples extends App {
  val v = (1, 1.4, "Hello")
  val x = v._3

  val symbols = Array("<", "-", ">")
  val counts = Array(2, 10, 31)
  val pairs = symbols.zip(counts)
  pairs.foreach(println)

}