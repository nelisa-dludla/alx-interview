#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const charactersUrl = data.characters;

    for (const character of charactersUrl) {
      await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(console.log(error));
          } else {
            const data = JSON.parse(body);
            resolve(console.log(data.name));
          }
        });
      });
    }
  }
});
