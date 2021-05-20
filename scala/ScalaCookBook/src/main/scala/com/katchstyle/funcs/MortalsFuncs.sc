val nums = 0 until 11
val alps = List("a", "b", "c", "d", "e")

nums.foreach( n => alps.foreach( a => {
    println(s"$n, $a")
}))


