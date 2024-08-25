// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.

const database = 'FirstDB';
const collection = 'CollectOne';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collection);


// Create a new document in the collection.
db.getCollection('CollectOne').insertOne({
    "name": "AleSb",
    "role": "Professional Student"
});

db.getCollection('CollectOne').getOne()