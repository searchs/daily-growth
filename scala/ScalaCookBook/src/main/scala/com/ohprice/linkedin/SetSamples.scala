package com.ohprice.linkedin

object SetSamples extends App {

  val fruit = Set("apple", "orange", "banana")
  var moreFruits = Set("kiwi", "pineapple")
  var nums = Set(1, 2, 3, 4, 5)
  var moreNums = Set(6, 7, 8, 9)

  println(nums.contains(5))
  println(nums(3))

  var mixed = fruit ++ nums
  println(mixed)

  nums -= 5
  println(nums)

  println(moreFruits.head)
  println(moreFruits.tail)

  println(moreFruits.isEmpty)
}
