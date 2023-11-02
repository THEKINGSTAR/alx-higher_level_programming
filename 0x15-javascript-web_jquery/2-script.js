/* eslint-disable */

/*
- JavaScript script that updates the text color
of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
*/

$(document).ready(function () {
  const redHeader = $('#red_header');

  redHeader.click(function () {
    const header = $('header');
    header.css('color', '#FF0000');
  });
});
