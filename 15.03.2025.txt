db.products.find()
{
  _id: 1,
  name: 'xPhone',
  price: 799,
  releaseDate: 2011-05-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 6.5,
    cpu: 2.66
  },
  color: [
    'white',
    'black'
  ],
  storage: [
    64,
    128,
    256
  ]
}
{
  _id: 2,
  name: 'xTablet',
  price: 899,
  releaseDate: 2011-09-01T00:00:00.000Z,
  spec: {
    ram: 16,
    screen: 9.5,
    cpu: 3.66
  },
  color: [
    'white',
    'black',
    'purple'
  ],
  storage: [
    128,
    256,
    512
  ]
}
{
  _id: 3,
  name: 'SmartTablet',
  price: 899,
  releaseDate: 2015-01-14T00:00:00.000Z,
  spec: {
    ram: 12,
    screen: 9.7,
    cpu: 3.66
  },
  color: [
    'blue'
  ],
  storage: [
    16,
    64,
    128
  ]
}
{
  _id: 4,
  name: 'SmartPad',
  price: 699,
  releaseDate: 2020-05-14T00:00:00.000Z,
  spec: {
    ram: 8,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256,
    1024
  ]
}
{
  _id: 5,
  name: 'SmartPhone',
  price: 599,
  releaseDate: 2022-09-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256
  ]
}
-- db.products.updateOne({_id:1}.{$inc:{price:50}})
-- SyntaxError: Unexpected token (1:30)

-- [0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mproducts[33m.[39mupdateOne({_id[33m:[39m[35m1[39m}[33m.[39m{$inc[33m:[39m{price[33m:[39m[35m50[39m}})
--  [90m   |[39m                               [31m[1m^[22m[39m[0m
db.products.updateOne({_id:1},{$inc:{price:50}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.products.find()
{
  _id: 1,
  name: 'xPhone',
  price: 849,
  releaseDate: 2011-05-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 6.5,
    cpu: 2.66
  },
  color: [
    'white',
    'black'
  ],
  storage: [
    64,
    128,
    256
  ]
}
{
  _id: 2,
  name: 'xTablet',
  price: 899,
  releaseDate: 2011-09-01T00:00:00.000Z,
  spec: {
    ram: 16,
    screen: 9.5,
    cpu: 3.66
  },
  color: [
    'white',
    'black',
    'purple'
  ],
  storage: [
    128,
    256,
    512
  ]
}
{
  _id: 3,
  name: 'SmartTablet',
  price: 899,
  releaseDate: 2015-01-14T00:00:00.000Z,
  spec: {
    ram: 12,
    screen: 9.7,
    cpu: 3.66
  },
  color: [
    'blue'
  ],
  storage: [
    16,
    64,
    128
  ]
}
{
  _id: 4,
  name: 'SmartPad',
  price: 699,
  releaseDate: 2020-05-14T00:00:00.000Z,
  spec: {
    ram: 8,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256,
    1024
  ]
}
{
  _id: 5,
  name: 'SmartPhone',
  price: 599,
  releaseDate: 2022-09-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256
  ]
}
db.products.updateOne({_id:1},{$inc:{price:-150}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.products.find()
{
  _id: 1,
  name: 'xPhone',
  price: 699,
  releaseDate: 2011-05-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 6.5,
    cpu: 2.66
  },
  color: [
    'white',
    'black'
  ],
  storage: [
    64,
    128,
    256
  ]
}
{
  _id: 2,
  name: 'xTablet',
  price: 899,
  releaseDate: 2011-09-01T00:00:00.000Z,
  spec: {
    ram: 16,
    screen: 9.5,
    cpu: 3.66
  },
  color: [
    'white',
    'black',
    'purple'
  ],
  storage: [
    128,
    256,
    512
  ]
}
{
  _id: 3,
  name: 'SmartTablet',
  price: 899,
  releaseDate: 2015-01-14T00:00:00.000Z,
  spec: {
    ram: 12,
    screen: 9.7,
    cpu: 3.66
  },
  color: [
    'blue'
  ],
  storage: [
    16,
    64,
    128
  ]
}
{
  _id: 4,
  name: 'SmartPad',
  price: 699,
  releaseDate: 2020-05-14T00:00:00.000Z,
  spec: {
    ram: 8,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256,
    1024
  ]
}
{
  _id: 5,
  name: 'SmartPhone',
  price: 599,
  releaseDate: 2022-09-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256
  ]
}
db.products
vit.products
db.products.drop()
true
db.products.insertMany([
    { "_id" : 1, "name" : "xPhone", "price" : 799, "releaseDate": ISODate("2011-05-14"), "spec" : { "ram" : 4, "screen" : 6.5, "cpu" : 2.66 },"color":["white","black"],"storage":[64,128,256]},
    { "_id" : 2, "name" : "xTablet", "price" : 899, "releaseDate": ISODate("2011-09-01") , "spec" : { "ram" : 16, "screen" : 9.5, "cpu" : 3.66 },"color":["white","black","purple"],"storage":[128,256,512]},
    { "_id" : 3, "name" : "SmartTablet", "price" : 899, "releaseDate": ISODate("2015-01-14"), "spec" : { "ram" : 12, "screen" : 9.7, "cpu" : 3.66 },"color":["blue"],"storage":[16,64,128]},
    { "_id" : 4, "name" : "SmartPad", "price" : 699, "releaseDate": ISODate("2020-05-14"),"spec" : { "ram" : 8, "screen" : 9.7, "cpu" : 1.66 },"color":["white","orange","gold","gray"],"storage":[128,256,1024]},
    { "_id" : 5, "name" : "SmartPhone", "price" : 599,"releaseDate": ISODate("2022-09-14"), "spec" : { "ram" : 4, "screen" : 5.7, "cpu" : 1.66 },"color":["white","orange","gold","gray"],"storage":[128,256]}
 ])
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5
  }
}
db..products.updateOne({
_id: 5},
{$min:{
price: 699}})
-- SyntaxError: Unexpected token (1:3)

-- [0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39m[33m.[39mproducts[33m.[39mupdateOne({
--  [90m   |[39m    [31m[1m^[22m[39m
--  [90m 2 |[39m _id[33m:[39m [35m5[39m}[33m,[39m
--  [90m 3 |[39m {$min[33m:[39m{
--  [90m 4 |[39m price[33m:[39m [35m699[39m}})[0m
-- db..products.updateOne({
-- _id: 5},
-- {$min:{
-- price: 699}})
-- SyntaxError: Unexpected token (1:3)

-- [0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39m[33m.[39mproducts[33m.[39mupdateOne({
--  [90m   |[39m    [31m[1m^[22m[39m
--  [90m 2 |[39m _id[33m:[39m [35m5[39m}[33m,[39m
--  [90m 3 |[39m {$min[33m:[39m{
--  [90m 4 |[39m price[33m:[39m [35m699[39m}})[0m
-- -- db..products.updateOne({_id: 5},{$min:{price: 699}})




-- SyntaxError: Unexpected token (1:3)

-- [0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39m[33m.[39mproducts[33m.[39mupdateOne({_id[33m:[39m [35m5[39m}[33m,[39m{$min[33m:[39m{price[33m:[39m [35m699[39m}})
--  [90m   |[39m    [31m[1m^[22m[39m
--  [90m 2 |[39m
--  [90m 3 |[39m
--  [90m 4 |[39m[0m
db.products.updateOne({_id: 5},{$min:{price: 699}})




{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 0,
  upsertedCount: 0
}
db.products.find()



{
  _id: 1,
  name: 'xPhone',
  price: 799,
  releaseDate: 2011-05-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 6.5,
    cpu: 2.66
  },
  color: [
    'white',
    'black'
  ],
  storage: [
    64,
    128,
    256
  ]
}
{
  _id: 2,
  name: 'xTablet',
  price: 899,
  releaseDate: 2011-09-01T00:00:00.000Z,
  spec: {
    ram: 16,
    screen: 9.5,
    cpu: 3.66
  },
  color: [
    'white',
    'black',
    'purple'
  ],
  storage: [
    128,
    256,
    512
  ]
}
{
  _id: 3,
  name: 'SmartTablet',
  price: 899,
  releaseDate: 2015-01-14T00:00:00.000Z,
  spec: {
    ram: 12,
    screen: 9.7,
    cpu: 3.66
  },
  color: [
    'blue'
  ],
  storage: [
    16,
    64,
    128
  ]
}
{
  _id: 4,
  name: 'SmartPad',
  price: 699,
  releaseDate: 2020-05-14T00:00:00.000Z,
  spec: {
    ram: 8,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256,
    1024
  ]
}
{
  _id: 5,
  name: 'SmartPhone',
  price: 599,
  releaseDate: 2022-09-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 5.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256
  ]
}
db.products.updateOne({_id: 5},{$min:{price: 499}})




{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.products.find()
{
  _id: 1,
  name: 'xPhone',
  price: 799,
  releaseDate: 2011-05-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 6.5,
    cpu: 2.66
  },
  color: [
    'white',
    'black'
  ],
  storage: [
    64,
    128,
    256
  ]
}
{
  _id: 2,
  name: 'xTablet',
  price: 899,
  releaseDate: 2011-09-01T00:00:00.000Z,
  spec: {
    ram: 16,
    screen: 9.5,
    cpu: 3.66
  },
  color: [
    'white',
    'black',
    'purple'
  ],
  storage: [
    128,
    256,
    512
  ]
}
{
  _id: 3,
  name: 'SmartTablet',
  price: 899,
  releaseDate: 2015-01-14T00:00:00.000Z,
  spec: {
    ram: 12,
    screen: 9.7,
    cpu: 3.66
  },
  color: [
    'blue'
  ],
  storage: [
    16,
    64,
    128
  ]
}
{
  _id: 4,
  name: 'SmartPad',
  price: 699,
  releaseDate: 2020-05-14T00:00:00.000Z,
  spec: {
    ram: 8,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256,
    1024
  ]
}
{
  _id: 5,
  name: 'SmartPhone',
  price: 499,
  releaseDate: 2022-09-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 5.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256
  ]
}
db.products.drop()
true
db.products.insertMany([
    { "_id" : 1, "name" : "xPhone", "price" : 799, "releaseDate": ISODate("2011-05-14"), "spec" : { "ram" : 4, "screen" : 6.5, "cpu" : 2.66 },"color":["white","black"],"storage":[64,128,256]},
    { "_id" : 2, "name" : "xTablet", "price" : 899, "releaseDate": ISODate("2011-09-01") , "spec" : { "ram" : 16, "screen" : 9.5, "cpu" : 3.66 },"color":["white","black","purple"],"storage":[128,256,512]},
    { "_id" : 3, "name" : "SmartTablet", "price" : 899, "releaseDate": ISODate("2015-01-14"), "spec" : { "ram" : 12, "screen" : 9.7, "cpu" : 3.66 },"color":["blue"],"storage":[16,64,128]},
    { "_id" : 4, "name" : "SmartPad", "price" : 699, "releaseDate": ISODate("2020-05-14"),"spec" : { "ram" : 8, "screen" : 9.7, "cpu" : 1.66 },"color":["white","orange","gold","gray"],"storage":[128,256,1024]},
    { "_id" : 5, "name" : "SmartPhone", "price" : 599,"releaseDate": ISODate("2022-09-14"), "spec" : { "ram" : 4, "screen" : 5.7, "cpu" : 1.66 },"color":["white","orange","gold","gray"],"storage":[128,256]}
 ])
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5
  }
}
db.products.updateOne({_id: 5},{ $mul: { price: 1.1 }})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.products.updateOne({_id: 1},{$mul: { "storage.0":2,"storage.1":2,"storage.2":2}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.products.drop()
true
db.products.insertMany([
    { "_id" : 1, "name" : "xPhone", "price" : 799, "releaseDate": ISODate("2011-05-14"), "spec" : { "ram" : 4, "screen" : 6.5, "cpu" : 2.66 },"color":["white","black"],"storage":[64,128,256]},
    { "_id" : 2, "name" : "xTablet", "price" : 899, "releaseDate": ISODate("2011-09-01") , "spec" : { "ram" : 16, "screen" : 9.5, "cpu" : 3.66 },"color":["white","black","purple"],"storage":[128,256,512]},
    { "_id" : 3, "name" : "SmartTablet", "price" : 899, "releaseDate": ISODate("2015-01-14"), "spec" : { "ram" : 12, "screen" : 9.7, "cpu" : 3.66 },"color":["blue"],"storage":[16,64,128]},
    { "_id" : 4, "name" : "SmartPad", "price" : 699, "releaseDate": ISODate("2020-05-14"),"spec" : { "ram" : 8, "screen" : 9.7, "cpu" : 1.66 },"color":["white","orange","gold","gray"],"storage":[128,256,1024]},
    { "_id" : 5, "name" : "SmartPhone", "price" : 599,"releaseDate": ISODate("2022-09-14"), "spec" : { "ram" : 4, "screen" : 5.7, "cpu" : 1.66 },"color":["white","orange","gold","gray"],"storage":[128,256]}
 ])
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5
  }
}
db.products.updateOne({_id: 1},{$unset:{price:""}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.products.find()
{
  _id: 1,
  name: 'xPhone',
  releaseDate: 2011-05-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 6.5,
    cpu: 2.66
  },
  color: [
    'white',
    'black'
  ],
  storage: [
    64,
    128,
    256
  ]
}
{
  _id: 2,
  name: 'xTablet',
  price: 899,
  releaseDate: 2011-09-01T00:00:00.000Z,
  spec: {
    ram: 16,
    screen: 9.5,
    cpu: 3.66
  },
  color: [
    'white',
    'black',
    'purple'
  ],
  storage: [
    128,
    256,
    512
  ]
}
{
  _id: 3,
  name: 'SmartTablet',
  price: 899,
  releaseDate: 2015-01-14T00:00:00.000Z,
  spec: {
    ram: 12,
    screen: 9.7,
    cpu: 3.66
  },
  color: [
    'blue'
  ],
  storage: [
    16,
    64,
    128
  ]
}
{
  _id: 4,
  name: 'SmartPad',
  price: 699,
  releaseDate: 2020-05-14T00:00:00.000Z,
  spec: {
    ram: 8,
    screen: 9.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256,
    1024
  ]
}
{
  _id: 5,
  name: 'SmartPhone',
  price: 599,
  releaseDate: 2022-09-14T00:00:00.000Z,
  spec: {
    ram: 4,
    screen: 5.7,
    cpu: 1.66
  },
  color: [
    'white',
    'orange',
    'gold',
    'gray'
  ],
  storage: [
    128,
    256
  ]
}
vit
