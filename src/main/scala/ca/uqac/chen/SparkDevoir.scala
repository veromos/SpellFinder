package ca.uqac.chen

import org.apache.spark.sql.{DataFrame, Dataset, Row, SparkSession}
import org.apache.spark.sql.functions.{size, explode}

object SparkDevoir {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder
      .appName(getClass.getSimpleName)
      .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    import spark.implicits._

    // EXERCICE 2
    val jsonPath = "data/spell_formatted_for_spark.json"
    val spells: DataFrame = spark.read.json(jsonPath)

    // EXERCICE 3
    val wizardV4Spells: Dataset[Row] = spells
      .withColumn("level", explode($"levels"))
      .filter($"level.class" === "sorcerer/wizard")
      .filter($"level.level" <= 4)
      .filter($"components"(0) === "V" && size($"components") === "1")

    wizardV4Spells.select("id", "name", "level.class", "level.level", "components", "spell_resistance").show(100, false)

    // EXERCICE 4
    spells.withColumn("level", explode($"levels")).createOrReplaceTempView("spell")

    val wizardV4SpellsSQL = spark.sql("""SELECT id, name FROM spell WHERE concat_ws(" ", components) == "V" AND level.level <= 4 AND level.class == "sorcerer/wizard"""")

    wizardV4SpellsSQL.show(100, false)
  }
}
