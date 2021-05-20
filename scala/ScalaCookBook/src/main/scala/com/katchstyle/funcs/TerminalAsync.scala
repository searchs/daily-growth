package com.katchstyle.funcs

import scala.concurrent.Future

trait TerminalAsync {

  def read(): Future[String]

  def write(t: String): Future[Unit]


}
