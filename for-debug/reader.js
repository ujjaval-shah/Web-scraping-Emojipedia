'use strict';

const fs = require('fs');

let rawdata = fs.readFileSync('categoryDetails.json');
let pageURLs = JSON.parse(rawdata);
console.log(pageURLs);

const urlList = pageURLs.categories.map((obj, index)=> `${index + 1}. ${obj.category} - ${obj.emoji} - ${obj.url}`);
console.log(urlList)