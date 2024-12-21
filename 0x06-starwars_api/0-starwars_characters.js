#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (!err && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(err);
      }
    });
  });
}

const url = 'https://swapi-api.hbtn.io/api/films/'.concat('' + arg);
async function main () {
  const film = await makeRequest(url);
  for (const cha of film.characters) {
    const character = await makeRequest(cha);
    console.log(character.name);
  }
}
main();
