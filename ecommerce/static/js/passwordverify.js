$(document).ready(function(){

  $('#passwordinput').keyup(function(){
    if($(this).val()==$('#verifypasswordinput').val()){
      $('#signupbutton').removeAttr("disabled");
    }
    else{
      $('#signupbutton').attr("disabled", "disabled");
    }
  });
  $('#verifypasswordinput').keyup(function(){
    if($(this).val() ==$('#passwordinput').val()){
      $('#signupbutton').removeAttr("disabled");
    }
    else{
      $('#signupbutton').attr("disabled", "disabled");
    }
  });


});
