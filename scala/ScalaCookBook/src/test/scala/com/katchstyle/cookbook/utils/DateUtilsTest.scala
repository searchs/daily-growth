package com.katchstyle.cookbook.utils

import com.katchstyle.cookbook.utils.DateUtils.getRunIdDayBefore
import org.scalatest.funsuite.AnyFunSuite

class DateUtilsTest extends AnyFunSuite {

  test("testCleanIngestDate") {
    val result = getRunIdDayBefore("2024-03-01_LY")
    assert(result === "2024-02-29_LY")
  }

  test("testGetRunIdDayBefore") {

  }

}
