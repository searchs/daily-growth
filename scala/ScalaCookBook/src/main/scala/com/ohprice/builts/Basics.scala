package com.ohprice.builts

object Basics extends App {

  val s = "eggs, milk, butter, Coco Puffs"

  s.split(",").map(_.trim.capitalize).foreach(println)

  val numPatterns = "[0-9]+".r
  val address = "123 Main Street Suite 202"
  val match1 = numPatterns.findFirstIn(address)
  println(match1)

  val match2 = numPatterns.findAllIn(address)
  match2.foreach(println)

  val strAddress = "Dancing corner with multiple"
  val result = numPatterns.findFirstIn(strAddress).getOrElse("No Match")
  println(result)

  //Replace numbers in parsed string
  val addy = "123 Flush Street Suite 3005 Union blocks".replaceAll("[0-9]", "x")
  println(addy)

  //AlphaNumeric pattern matching
  val pattern = "([0-9]+) ([A-Za-z]+)".r
  val pattern(count, fruit) = "203 Oranges"
  println(count, fruit)

  println(Short.MaxValue, Short.MinValue)


  //  Randoms
  val r = scala.util.Random
  println(r.nextInt)
  println(r.nextInt(100))
  println(r.nextFloat)

  val numList = 0 to r.nextInt(10)
  numList.foreach(println)

  //Formatters
  val formatter = java.text.NumberFormat.getIntegerInstance
  println(formatter.format(1000))
  println(formatter.format(100000))
  println(formatter.format(10000000))

  val fmt = java.text.NumberFormat.getInstance
  println(fmt.format(124258.0978))

  val fmtCur = java.text.NumberFormat.getCurrencyInstance
  println(fmtCur.format(123456.890))

  import java.util.{Currency, Locale}

  val gb = Currency.getInstance(new Locale("gb", "GB"))
  //  fmtCur.setCurrency("gb")
  fmtCur.setCurrency(gb)
  println(fmtCur.format(1000964.342))

  def obj: String = "Scala Cookbook for me"

  obj
}

