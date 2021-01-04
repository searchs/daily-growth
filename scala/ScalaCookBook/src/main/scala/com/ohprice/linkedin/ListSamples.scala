package com.ohprice.linkedin

object ListSamples extends App {

  var l = List(3.0, 5, 'a')
  var ll = 1 :: 2 :: 3 :: 4 :: 5 :: Nil
  var l3 = List.range(10, 20)

  var l4 = l ::: ll
  var sum = 0
  l3.foreach(sum += _)
  println(sum)


}
