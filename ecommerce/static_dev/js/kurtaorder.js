$(document).ready(function(){

  var hexDigits = new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f");
  function hex(x) {
    return isNaN(x) ? "00" : hexDigits[(x - x % 16) / 16] + hexDigits[x % 16];
  }
  function rgb2hex(rgb) {
   rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
   return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
  }
  $('.color-value').click(function(){
    var color = $(this).css("background-color");
    var colorhex = rgb2hex(color);
    $('.color-value').html('');
    $(this).html('❤');
    $('#ordercolor').val(colorhex);
  });
  $('.size-value').change(function(){
    var total = parseInt($('input[name="udf1"]').val()) +
                parseInt($('input[name="udf2"]').val()) +
                parseInt($('input[name="udf3"]').val()) +
                parseInt($('input[name="udf4"]').val()) +
                parseInt($('input[name="udf5"]').val());
    var ordertotal = total*230 + 500;
    $("#orderno").html(total);
    $(".size-total-value").val(total);
    $("#purchasetotal").val(ordertotal);
    $("#purchaseamount").html(ordertotal)
  });




});
