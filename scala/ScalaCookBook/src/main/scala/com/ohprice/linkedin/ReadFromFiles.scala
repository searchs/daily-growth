package com.ohprice.linkedin

import io.Source._

object ReadFromFiles extends App {

val fileName = "src/colors.txt"
  for(line <- fromFile(fileName).getLines()){
    println(line.capitalize)
  }


  var poemLines = fromFile("src/poems.txt").getLines().toList
  poemLines.foreach(println)


}
