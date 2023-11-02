/* eslint-disable */

/*
Write a JavaScript script that fetches the character name
from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
*/
$(document).ready(function () {
    $('DIV#character').click(function () {
        const content = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
        $.get(content, function(data)
        {
            const contentName = data.name;
            $('DIV#character').text(contentName);
        });
    });
  });
  