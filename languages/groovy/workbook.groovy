def s = 'this is a string ${1+1}'
println s

println "Another interpolation is here: ${1+1}"

Range r = 1..101
println r[-3]
println r.from

def nums = [1,2,3,4,5,6,7,,8,9,10]
//nums.each { println it }
nums.each { n -> println n }


nums.eachWithIndex {n, idx -> 
println "nums[$idx] == $n}"
}

nums.collect { it * 2 } //map
.findAll {it % 3 == 0 } //reduce
.sum() //reduce


List strings = 'this is a list of strings'.split()
strings.collect { it.size() } //
println strings*.size() //spread dot operator - applies method to each element in the collection
println strings.size() // applies method to the collection


def mp = [k1: 'v1', k2: 'v2', k3: 'v3']
mp.collect {k, v -> println mp[k] }

//Playing with Google's GeoCode APIs
def gmap_uri = 'http://www.google.com'
def results = gmap_uri.toURL().text
println results.size()
// println results

String base = 'https://maps.googleapis.com/maps/api/geocode/xml?'
def encoded = ['10 Fawcett Street', 'Cambridge', 'MA'].collect {
    URLEncoder.encode(it, 'UTF-8')
}.join(',')

def qs = "address=$encoded"

//"$base$qs".toURL().text
//Playing with XML results
def root = new XmlSlurper().parse("$base$qs")

def loc = root.result[0].geometry.location
println "(${loc.lat}, ${loc.lng})"

//Playing with JSON 
import groovy.json.*
String base = 'http://api.icndb.com/jokes/random?'

def qs = [limitTo: '[nerdy]', firstName:'Guillaume', lastName: 'Laforge'].collect {
    k,v -> "$k=$v"}.join('&')
    
String jsonTxt = "$base$qs".toURL().text
def json = new JsonSlurper().parseText(jsonTxt)
println json.value.joke

String name;

String n = (name != null && name.size() > 0 ? name: 'World')
n = name ?: 'World'

println "Allo, $n"

//Implementing Sorting Algo in Groovy
List strings = 'this is a list of strings'.split()
println strings

import java.Collections.*

//Java natural sort
Collections.sort(strings)
println strings

// Java sort by length
Collections.sort(strings, new Comparator<String>(){
    int compare(String s1, String s2){
        s1.size() <=> s2.size()
    }
})

println strings
assert strings*.size() == [1,2,2,4,4,7]


//Groovy natural sort
println strings.sort(false, new Comparator<String>(){
    int compare(String s1, String s2){
        s1.size() <=> s2.size()
    }
})


//Groovy reverse length sort with a 2-param closure
println strings.sort(false) {s1,s2 ->
s2.size() <=> s1.size()
}


//Groovy length sort with a 1-para closure
println "Single Params Closure"
println strings.sort(false) {it.size()}

//Groovy sort by length, then equal lenths alphabethically
println strings.sort(false) {String s1, String s2 ->
s1.size() <=> s2.size() ?: s2 <=> s1
}



//Addition
List cts = [3,1,4,1,5,9,2,6,5]
println cts

//Groovy using collect
assert 72 == cts.collect { it * 2 }.sum()

//Reduce to a problem already solved
assert 72 == cts.sum() * 2


//Another sweet way
assert 72 == cts.sum { it * 2 }

//Using a Spread dot 

assert 72 == cts*.multiply(2).sum()

//Just double the collection
assert 72 == (cts * 2).sum()


//Using Groovy Inject - like Scala's Reduce?
assert 72 == cts.inject(0) {acc, val ->
acc + val * 2
}

