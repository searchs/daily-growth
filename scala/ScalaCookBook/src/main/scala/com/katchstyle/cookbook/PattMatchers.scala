package com.katchstyle.cookbook

object PattMatchers extends App {

  val numPatterns = "[0-9]+".r

  val addy = "243 Wise Street Suite 506 New York"

  val matchWithDefault = numPatterns.findFirstIn(addy).getOrElse("No Match!")
  val matchWithNoDef = numPatterns.findAllIn(addy)

  println(matchWithDefault)
  println(matchWithNoDef)


  val moviesZipCodes = "movies (\\d{5})".r
  val moviesNearCityStateRE = "movies near ([a-z]+), ([a-z]{2})".r

  def getSearchResults(zip: String) = ???
  def getSearchResults(city: String, state: String) = ???

  def userMovies(textUserTyped: String) = textUserTyped match {
  case moviesZipCodes(zip) => getSearchResults(zip)
  case moviesNearCityStateRE(city, state) => getSearchResults(city, state)
  case _ => println("did not match a regex")
}

  //  Test data

  //  "movies near 80301"
  //  "movies 80301"
  //  "80301 movies"
  //  "movie: 80301"
  //  "movies: 80301"
  //  "movies near boulder, co"
  //  "movies near boulder, colorado"

implicit class StringImprovements(s: String){
  def increment = s.map(c => (c + 1).toChar)
}

  val result = "HAL".increment
  println(result)



}
