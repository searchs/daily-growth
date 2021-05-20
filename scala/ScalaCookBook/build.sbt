name := "ScalaCookBook"

version := "0.1"

//scalaVersion in ThisBuild := "2.12.12"
scalaVersion in ThisBuild := "2.13.5"
scalacOptions in ThisBuild ++= Seq(
  "-language:_",
  "-Ypartial-unification",
  "-Xfatal-warnings"
)

libraryDependencies ++= Seq(
  "org.scalatest" %% "scalatest" % "3.3.0-SNAP2" % Test,
  "org.scalaz" %% "scalaz-core" % "7.4.0-M6",
  "com.github.mpilquist" %% "simulacrum" % "0.19.0"

)
