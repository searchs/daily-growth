val scala3Version = "3.2.0"

lazy val root = project
  .in(file("."))
  .settings(
    name := "Thrive",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies ++= Seq(
      "org.scalatest" %% "scalatest" % "3.2.14" % Test
    )
  )
