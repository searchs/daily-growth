package com.ohprice.linkedin

import java.io._
import scala.io.Source._

object ErrorHandling extends App {

  try {
    for (line <- fromFile("noFile.txt").getLines())
      println((line.capitalize))
  } catch {
    case e: FileNotFoundException => println("File not found")
    case _: Exception => println("Program has error")
  }

  try {
    var quotient = 10/0
  } catch {
    case e: ArithmeticException => println("Do not divide by Zero(0)")
  }

}
