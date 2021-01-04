package com.ohprice.linkedin

object PatternMatching extends App {

  def greekAlphabet(letter: Char) = {
    letter.toLower match {
//      case 'a' | 'A' => "Alpha"
      case 'a'  => "Alpha"
      case 'b' => "Beta"
//      case 'b' | 'B' => "Beta"
      case _ => "Not yet generated!"
    }
  }


  println("The Greek letter for A is " + greekAlphabet('A'))
  println("The Greek letter for B is " + greekAlphabet('B'))
  println("The Greek letter for C is " + greekAlphabet('C'))


  def max(x: Int, y: Int) =  x> y match {
    case true => x
    case false => y
  }

println(max(3,5))
println(max(5,4))
println(max(4,4))

}
