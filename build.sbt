name := "SpellFinder"

version := "1.0"

scalaVersion := "2.12.8"

val SPARK_VERSION = "2.4.4"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % SPARK_VERSION,
  "org.apache.spark" %% "spark-core" % SPARK_VERSION
)