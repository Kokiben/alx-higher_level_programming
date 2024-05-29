/**
 * JavaScript script using JQuery API
 */

$(document).ready(function() {
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
  });
});
