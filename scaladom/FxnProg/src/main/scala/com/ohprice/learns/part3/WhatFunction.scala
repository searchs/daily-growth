package com.ohprice.jv
package com.ohprice.learns.part3

object WhatFunction extends  App{

val doubler = new MyFunction[Int, Int] {
  override def apply(element: Int): Int = element * 2
}

println(doubler(2))


val stringToIntConverter = new Function1[String, Int]{
  override def apply(str: String): Int = str.toInt
}

println(stringToIntConverter("3") + 4)


}


trait MyFunction[A,B] {
  def apply(element: A): B
}
