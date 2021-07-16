$(document).ready(function(){
    const modal = $('.modal')
    slideIndex = 1;

    $('.showModal').click(function(event){

        var storyid = event.currentTarget.name;

        $.ajax({
          type: 'GET',
          url: '/stories/showMedia/' + storyid,
          datatype: 'json',

          success: function(data){
            $.each(data, function(i,v){
              var n = parseInt(i) + 1;
              if(v.content.slice(v.content.length - 3) === 'mp4'){
                var div_slides_html = '<div class="mySlides fade"><div class="numbertext">' + n + ' / ' + data.length + '</div><video width="1000" controls="controls" preload="metadata"><source src="/media/' + v.content + '#t=0.5" type="video/mp4"></video><div class="text">' + v.caption + '</div></div>'
              }
              else{
                var div_slides_html = '<div class="mySlides fade"><div class="numbertext">' +  n + ' / ' + data.length + '</div><img src="/media/' + v.content + '"style="width:100%" /><div class="text">' + v.caption + '</div></div>'
              }
              $('#jsondata').append(div_slides_html);
            });
          },
          complete: function(){
            showSlides(slideIndex);
          }
        })

        modal.addClass('is-active');
    });

    $('#closeModal').click(function (event) {
        const slides = document.getElementById('jsondata')
        slides.innerHTML = '';
        modal.removeClass('is-active')
    });
});

// story slider js 

// showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  // var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  // for (i = 0; i < dots.length; i++) {
  //     dots[i].className = dots[i].className.replace(" active", "");
  // }
  slides[slideIndex-1].style.display = "block";
  // dots[slideIndex-1].className += " active";
}

// index slider js 
var slideI = 1;
showslides(slideI);

// Next/previous controls
function plusslides(n) {
  showslides(slideI += n);
}

// Thumbnail image controls
function currentslide(n) {
  showslides(slideI = n);
}

function showslides(n) {
  var i;
  var slides = document.getElementsByClassName("myslides");
  // var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideI = 1}
  if (n < 1) {slideI = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  // for (i = 0; i < dots.length; i++) {
  //     dots[i].className = dots[i].className.replace(" active", "");
  // }

  slides[slideI-1].style.display = "block";
  // dots[slideIndex-1].className += " active";
}

// like ajax request 
 