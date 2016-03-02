var main = function() {
  /* Push the body and the nav over by 285px over */
  $('.icon-menu').click(function() {


    $('.menu').animate({
      left: "0px"
    }, 200);

    $('.content').animate({
      left: "5%",
      /*right: "14%"*/
    }, 200);
  });

  /* Then push them back */
  $('.icon-close').click(function() {

      $('.menu').animate({
      left: "-200px"
    }, 200);

    $('.content').animate({
      left: "0%",
      /*right: "22%"*/
    }, 200);
  });

  $('.artworks-list li a').click(function(event) {
        event.preventDefault();
        currentPhoto=document.getElementsByClassName('photo-slides')[0];
        currentPhoto.src=$(this).attr('href');
        $('.photo-slides').fadeIn(600, function() {

        });
    });

};


$(document).ready(main);