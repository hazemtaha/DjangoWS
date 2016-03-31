$(function(){
	//$('.nav-tabs').tab();
	$('.ts').click(function(){
		$('.ts').each(function(i){
			$(this).removeClass('active');
		});
		$(this).addClass('active');
	});

    $('.Hts').click(function(){
		$('.Hts').each(function(i){
			$(this).removeClass('active');
		});
		$(this).addClass('active');
	});



});
