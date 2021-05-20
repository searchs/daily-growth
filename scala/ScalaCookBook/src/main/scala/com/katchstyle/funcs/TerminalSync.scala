package com.katchstyle.funcs

trait TerminalSync {
  def read(): String

  def write(t: String): Unit
}
