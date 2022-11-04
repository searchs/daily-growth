package com.katchstyle.cookbook

object Numerics extends App {

  @throws(classOf[NumberFormatException])
  def toInt(s: String) = s.toInt


  def toIntMatch(s: String): Option[Int] = {
    try {
      Some(s.toInt)
    } catch {
      case e: NumberFormatException => None
    }
  }

 println(toInt("40"))

  println(toIntMatch("Hola!"))

val names = Map("fname" -> "Roberto", "lname" -> "Goren")
  names.foreach(println)
  for ((k,v) <- names) { println(s"Value: $v, Key: $k")}
}
