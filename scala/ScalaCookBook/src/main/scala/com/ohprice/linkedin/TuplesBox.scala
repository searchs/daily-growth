package com.ohprice.linkedin

object TuplesBox extends App  {

    val v = (1, 1.4, "Hello")
    val x = v._3

    val symbols = Array("<", "-", ">")
    val counts = Array(2, 10, 31)
    val pairs = symbols.zip(counts)
    pairs.foreach(println)


  for((s,n) <- pairs) print(s*n)
  println


//  More Examples
  def divide10(n: Int): Tuple2[Float,Int] = (n/10, n%10)

  val (tens,ones) = divide10(99)
  println(tens, ones)

  }
