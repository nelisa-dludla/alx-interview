#!/usr/bin/node

const filmId = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  }
});
