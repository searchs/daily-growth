package com.ohprice.linkedin

object ChallengeCollections extends App {
  //AVG of array of num
  //  MIN/Max, SUM

  def SumArray(arr: Array[Int]): Int = {
    var sum = 0
    for (v <- arr) yield sum += v
    //    arr.foreach(sum += _)
    sum
  }

  def avgArray(arr: Array[Int]): Double = {
    SumArray(arr) / arr.length
  }

  def maxValue(arr: Array[Int]): Int = {
    //    arr.reduceLeft(max)
    var mx = arr(0)
    for (v <- arr) if (v > mx) mx = v
    mx

  }

  def max(a: Int, b: Int) = if (a > b) a else b

  def min(a: Int, b: Int) = if (a < b) a else b


  def minValue(arr: Array[Int]): Int = {
    //    arr.reduceLeft(min)
    var mn = arr(0)
    for (v <- arr) if (v < mn) mn = v
    mn
  }


  val data = List.range(0, 11).toArray

  println(s"Sum: ${SumArray(data)}")
  println(s"Average: ${avgArray(data)}")
  println(s"Max: ${maxValue(data)}")
  println(s"Min: ${minValue(data)}")


}