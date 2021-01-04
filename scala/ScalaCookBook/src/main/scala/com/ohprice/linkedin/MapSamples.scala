package com.ohprice.linkedin

object MapSamples extends  App{


  var groceries = Map(1 -> "milk", 2 -> "bread", 3-> "juice", 4 -> "egss")
  groceries = groceries + (5 -> "hashbrowns")
  println(groceries.get(5))

  groceries.getOrElse(6,"No Match!")
  for(v <- groceries.values) println(v)

  println("=" * 85)
  var z = for((k,v) <- groceries) yield (v,k)
  println(z)

  z.foreach(println)

}
