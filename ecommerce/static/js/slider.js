$(document).ready(function(){

  $('.edit-button').click(function(){
    $('.account-edit').removeAttr("disabled");
  });
  $('#cancel-button').click(function(){
    location.reload();
  });
});
