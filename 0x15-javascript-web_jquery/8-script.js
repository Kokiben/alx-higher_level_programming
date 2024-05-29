/**
 * JavaScript script using JQuery API
 */

$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function(response) {
      response.results.forEach(function(movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function() {
      $('#list_movies').append('<li>Error fetching movies</li>');
    }
  });
});
