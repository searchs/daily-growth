package com.katchstyle.oreily.nlytics


sealed trait Message

case class Draw(shape: Shape) extends Message
case class Response(msg: String) extends  Message
case object Exit extends Message

object Basket {

}
