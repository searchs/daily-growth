package com.ohprice.linkedin

object ArraySamples extends App {

  var nums = new Array[Any](10)
  var furniture = Array("chair", "sofa", "table", "bed")
  for (f <- furniture) println(f)

  println(furniture(0))
  var a = Array(1, 2, 3, 4, 5)
  var results = for (n <- a) yield 2 * n
  results.foreach(println)

  var even = for (n <- a if n % 2 == 0) yield n
  even.foreach(println)
}
