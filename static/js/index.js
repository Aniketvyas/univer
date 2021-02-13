// var a = document.getElementsByClassName('dropdown');
//   a.addEventListener('click',function(){
//     if (window.innerWidth<1200){
//       console.log(true); 
//     var b = document.children('dropdown-menu').style.display="block";
//     }
//   });
// $('dropdown').click(function(){
//   if(window.innerWidth>1200){
//     $(".dropdown-toggle").attr("data-toggle", "dropdown");
//   }
// })

$('.dropdown').hover(function() {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
  }, function() {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
  });
var degreeMenu = document.getElementById('degree');
        var specializationMenu = document.getElementById('specialization');
        // console.log(specializationMenu[0].data);

        $('#degree').on('change', function() {
            var selected = $(this).val();
            $("#specialization option").each(function(item){
                console.log(selected) ;  
                var element =  $(this) ; 
                console.log(element.data("tag")) ; 
                if (element.data("tag") != selected){
                    element.hide() ; 
                }else{
                    element.show();
                }
            }) ; 
            
            $("#specialization").val($("#expertCat option:visible:first").val());
            
        });
        
        
var a = document.getElementsByClassName('dropdown-toggle')
for(i=0;i<a.length;i++){
    a[i].addEventListener('click',function(){
        console.log(i);
        console.log(a);
    })
}
$(document).click(function (e) {
    e.stopPropagation();
    var container = $(".dropDown");

    //check if the clicked area is dropDown or not
    if (container.has(e.target).length === 0) {
        $('.subMenu').hide();
    }
})

//  console.log(document.getElementsByClassName('dropdown-toggle')[0].ariaExpanded);
