var main = function() {
  /* Push the body and the nav over by 285px over */

  $('.fancybox').fancybox({
        nextClick: true,
		padding: 0,
        openEffect	: 'none',
		closeEffect	: 'none',
        helpers : {
            title: null,
            overlay : {
                css: {
                    'background' : 'rgba(0,0,0,0.9)'

                }
            }
        }

	});
};


$(document).ready(main);