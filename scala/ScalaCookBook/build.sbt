name := "ScalaCookBook"

version := "0.2.2"

scalaVersion in ThisBuild := "3.2.0"
//scalacOptions in ThisBuild ++= Seq(
//  "-language:_",
//  "-Ypartial-unification",
//  "-Xfatal-warnings"
//)

libraryDependencies ++= Seq(
  "org.scalatest" %% "scalatest" % "3.2.14" % Test,
)
//"org.scalatest" %% "scalatest" % "3.3.0-SNAP2" % Test,
