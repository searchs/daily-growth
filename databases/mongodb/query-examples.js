// MongoDB query examples migrated from searchs/mongobox.

db.movieDetails.find({
    rate: "PG-13"
}).pretty();

db.movieDetails.find({year: 2013, rated: "PG-13"}, {"awards.wins":0}).pretty()

// Equality Match
db.movieDetails.find({
    "tomato.meter": 100
}).count(); // nested document

db.movieDetails.find({
    "writers": ["Ethan Coen", "Joel Coen"]
}).count();

db.movieDetails.find({
    "actors.0": "Jeff Bridges"
}).pretty(); // get movies where Jeff is main actor

// Cursors
var c = db.movieDetails.find();
var doc = function() {
    return c.hasNext() ? c.next() : null;
}

c.objLeftInBatch();

// Projections
db.movieDetails.find({ rated: "PG-13" }, { title: 1 }).pretty();
db.movieDetails.find({ rated: "PG-13" }, { title: 1, _id: 0 }).pretty();

// Comparison Operators
db.movieDetails.find({ runtime: { $gt: 90 } }).pretty();

db.movieDetails.find(
    { runtime: { $gt: 90 } },
    { title: 1, runtime: 1, _id: 0 }
).pretty();

db.movieDetails.find({
    runtime: { $gte: 90, $lte: 129 }
}).pretty();

db.movieDetails.find(
    { "tomato.meter": { $gte: 95 }, runtime: { $gte: 180 } },
    { title: 1, runtime: 1, _id: 0 }
).pretty();

// Not Equal / In
db.movieDetails.find({ rated: { $ne: "UNRATED" } }).count();
db.movieDetails.find({ rated: { $in: ["G", "PG"] } }).pretty();

// Element / Type Operators
db.movieDetails.find({ "tomato.meter": { $exists: true } }).count();
db.movieDetails.find({ "_id": { $type: "string" } }).count();

// Logical Operators
db.movieDetails.find({
    $or: [
        { "tomato.meter": { $gt: 95 } },
        { "metacritic": { $gt: 88 } }
    ]
}).pretty();

db.movieDetails.find({
    $and: [
        { "tomato.meter": { $gt: 95 } },
        { "metacritic": { $gt: 88 } }
    ]
}).pretty();

db.movieDetails.find({
    $and: [
        { "metacritic": { $ne: null } },
        { "metacritic": { $exists: true } }
    ]
}).pretty();

// Regex Operators
db.movieDetails.find({}, { "awards.text": 1, _id: 0 }).pretty();
db.movieDetails.find({ "awards.text": { $regex: /^Won\s.*/ } });
db.movieDetails.find(
    { "awards.text": { $regex: /^Won\s.*/ } },
    { title: 1, "awards": 1, _id: 0 }
);

// Array Operators
db.movieDetails.find({ genres: { $all: ["Comedy", "Crime", " Drama"] } }).pretty();
db.movieDetails.find({ countries: { $size: 1 } }).pretty();

// $elemMatch
db.movieDetails.find({
    boxOffice: {
        $elemMatch: {
            country: "UK",
            revenue: { $gt: 15 }
        }
    }
});
