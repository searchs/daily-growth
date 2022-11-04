package com.katchstyle.cookbook.utils


import java.time._
import java.time.format.DateTimeFormatter

object DateUtils extends App {


  val runIdFormat = "(\\d{4})-([01][0-9]+)-([012][0-9]+)_([A-Za-z]+)".r

  def getRunIdDayBefore(runId: String): Option[String] = runId match {

    case runIdFormat(year, month, day, ee) => Some(LocalDate.parse(s"$year-$month-$day",
      DateTimeFormatter.ofPattern("yyyy-MM-dd"))
      .minusDays(1) + "_" + ee)
    case _ => None
  }


  println(getRunIdDayBefore("2022-10-01_HQ"))
  println(getRunIdDayBefore("2024-03-01_LPYEAR"))
  println(getRunIdDayBefore("2022-10-01_"))
  println(getRunIdDayBefore("2022-10-01"))
  println(getRunIdDayBefore(""))

  //Dates in various formats
  def getDateOnly(rawString: String): String = rawString.toUpperCase().replace(".", "").split("E").head

  def removeDots(rawStr: String): String = rawStr.replaceAll(".", "")


  def breakIntoDateComponents(userDate: String): String = userDate.length match {
    case 8 => userDate.substring(0, 4) + "-" + userDate.substring(4, 6) + "-" + userDate.substring(6, 8)
    case 7 => userDate.substring(0, 4) + "-" + userDate.substring(4, 6) + "-0" + userDate.substring(6, 7)
    case _ => userDate
  }


  def cleanDateByLength(dateStr: String): String = breakIntoDateComponents(getDateOnly(dateStr))
  //  def cleanDateByLength(dateStr: String): String = breakIntoDateComponents(removeInvalidCharacters(dateStr))

  def cleanupDates(userDate: String): String = userDate match {
    case s => "Oops"
    case _ => "Invalid date"
  }

  //Test
  println(cleanDateByLength("20180930"))
  println(cleanDateByLength("2018091"))
  println(cleanDateByLength("20170921E5"))

  val blockPattern = "(\\d{4})\\S(\\d{2})\\S(\\d{2})".r
  val dateInFull = "(\\d{4})\\S(\\d{2})\\S(\\d{2})(\\s+\\w[A-Za-z0-9]+)".r
  val dateWithComplexE = "(\\d{4})(\\d{2})(\\d{2})".r
//  val dateWithFullDetails = "(\\d{4})-(\\d{2})-(\\d{2})\\s".r
  val dateWithEightDigits = "(\\d{4})(\\d{2})(\\d{2})([A-Za-z]+)([0-9]+)".r
  val dateWithSevenDigits = "(\\d{4})(\\d{2})(\\d)".r
//  val dateWithTimezone = "(\\d{4})\\S(\\d{2})\\S(\\d{2})(\\s+)(\\d{2}):(\\d{2}):(\\d{2})(\\[a-zA-Z])".r
  val dateWithTimezone = "(\\d{4})\\S(\\d{2})\\S(\\d{2})(\\s+)(\\w+)([a-zA-Z0-9]+\\w)".r
  val reg = "(\\d{4})\\S(\\d{2})\\S(\\d{2})(T)(\\d{2}):(\\d{2})".r.unanchored


  def cleanDate(rawDate: String): String = rawDate.replace(".", "") match {
    case blockPattern(year, month, day) => s"F- $year-$month-$day" //ok
    case dateWithComplexE(year, month, day, _*) => s"E- $year-$month-$day" //ok
    case dateWithSevenDigits(year, month, day, _*) => s"7- $year-$month-0$day" //ok
    case dateWithEightDigits(year, month, day, _*) => s"8- $year-$month-$day" //ok
    case dateInFull(year, month, day, _*) => s"DaF- $year-$month-$day"
    case dateWithTimezone(year, month, day,_*) => s"TZ- $year-$month-$day"
    case reg(year, month, day, _*) => s"RG- $year-$month-$day" //ok
    case _ => s"Untouched $rawDate"
  }


  println("=========== DATE CLEANER ================")

  println(cleanDate("20180430E6"))
  println(cleanDate("2.0190631E6"))
  println(cleanDate("20210823Z6"))
  println(cleanDate("20211225"))
  println(cleanDate("2023012"))
  println(cleanDate("2023-01-12"))
  println(cleanDate("2025/03/16"))
  println(cleanDate("2020-05-22 00:01:00Z"))
  println(cleanDate("2018-08-22T19:10:53.094Z"))


}
