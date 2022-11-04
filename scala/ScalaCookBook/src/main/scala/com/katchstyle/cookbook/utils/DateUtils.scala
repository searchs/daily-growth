package com.katchstyle.cookbook.utils


import java.time._
import java.time.format.DateTimeFormatter
import scala.util.matching.{Regex, UnanchoredRegex}

object DateUtils extends App {


  val runIdFormat: Regex = "(\\d{4})-([01][0-9])-([012][0-9])_([A-Za-z]{2})".r

  def getRunIdDayBefore(runId: String): Option[String] = runId match {

    case runIdFormat(year, month, day, ee) =>
      val rawRunId = LocalDate.parse(s"$year-$month-$day",
      DateTimeFormatter.ofPattern("yyyy-MM-dd"))
      .minusDays(1)
      val finalRunId = rawRunId + "_" + ee
      Some(finalRunId)
    case _ => None
  }

  println(getRunIdDayBefore("2022-10-01_HQ"))
  println(getRunIdDayBefore("2024-03-01_LP"))
  println(getRunIdDayBefore("2022-10-01_"))
  println(getRunIdDayBefore("2022-10-01"))
  println(getRunIdDayBefore(""))

  val basePattern: Regex = "(\\d{4}\\S\\d{2}\\S\\d{2})".r
  val basePatternWithSeparator: Regex = "(\\d{4})\\S(\\d{2})\\S(\\d{2})".r
  val dateWithComplexE: Regex = "(\\d{4})(\\d{2})(\\d{2})".r
  val dateWithEightDigits: Regex = "(\\d{4})(\\d{2})(\\d{2})([A-Za-z0-9]+)".r
  val dateWithSevenDigits: Regex = "(\\d{4})(\\d{2})(\\d)".r
  val dateWithSpaceLong: UnanchoredRegex = "(\\d{4})\\S(\\d{2})\\S(\\d{2})(\\s+)(\\d{2}):(\\d{2})".r.unanchored
  val dateWithTimezone: UnanchoredRegex = "(\\d{4})\\S(\\d{2})\\S(\\d{2})(T)(\\d{2}):(\\d{2})".r.unanchored


  def cleanIngestDate(rawDate: String): String = rawDate.replace(".", "") match {
    case basePattern(year, month, day) => s"Base: $year-$month-$day" //ok
    case basePatternWithSeparator(year, month, day) => s"BaseS: $year-$month-$day" //ok
    case dateWithComplexE(year, month, day, _*) => s"Complex: $year-$month-$day" //ok
    case dateWithSevenDigits(year, month, day, _*) => s"S7: $year-$month-0$day" //ok
    case dateWithEightDigits(year, month, day, _*) => s"E8 - $year-$month-$day" //ok
    case dateWithSpaceLong(year, month, day, _*) => s"SL: $year-$month-$day"
    case dateWithTimezone(year, month, day, _*) => s"TZ: $year-$month-$day" //ok
    case _ => s"Raw: $rawDate"
  }


  println("=========== DATE CLEANER TESTCASES ================")
  println(cleanIngestDate("20180430E6"))
  println(cleanIngestDate("2.0190631E6"))
  println(cleanIngestDate("20210823Z6"))
  println(cleanIngestDate("20211225"))
  println(cleanIngestDate("2023012"))
  println(cleanIngestDate("2023-01-13"))
  println(cleanIngestDate("2025/03/16"))
  println(cleanIngestDate("2020-05-22 00:01:00Z"))
  println(cleanIngestDate("2018-08-02T19:10:53.094Z"))


}
