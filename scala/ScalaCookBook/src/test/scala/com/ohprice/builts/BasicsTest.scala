package com.ohprice.builts

import org.scalatest.funsuite.AnyFunSuite

class BasicsTest extends AnyFunSuite {
  test("check obj output") {
    assert(Basics.obj == "Scala Cookbook for me")
    println("End of tests")
  }

}
