//modal
// Get the modal
var modal = document.getElementById('myModal');
// Get the image and insert it inside the modal - use its "alt" text as a caption

var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
$(function() {
    $('.fa-eye').on('click', function() {
        modal.style.display = "block";
        captionText.innerHTML = $(this).parent().parent().find('img').attr('alt');
        $('.modal-content').attr('src', $(this).parent().parent().find('img').attr('src'));
//        $('#myModal').modal('show');  
        $('#myModal').modal('show');
    }); 
    var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
    span.onclick = function() { 
        modal.style.display = "none";
        window.location.reload(true);
    }
    
});




//$(function(){
//    $('.fa-eye').onclick = function(){
//    var img = $(this).parent().parent().find('img');
//    modal.style.display = "block";
//    modalImg.src = img.src;
//    captionText.innerHTML = img.alt;
//}
//});


// Get the <span> element that closes the modal




//timer
function updateTimer(deadline){
	var time = deadline - new Date(); //return differens between now and deadline
	return {
		'days': Math.floor(time/(1000*60*60*24)),
		'hours': Math.floor((time/(1000*60*60))%24),
		'minutes': Math.floor((time/1000/60)%60),
		'seconds': Math.floor((time/1000)%60),
		'total': time
	};
};

function animateClock(span){
	span.className = "turn";
	setTimeout(function(){
		span.className = "";
	}, 700);
}

function startTimer(id, deadline){
	var timerInterval = setInterval(function(){
		var clock = document.getElementById(id); //store element
		var timer = updateTimer(deadline);

		clock.innerHTML = '<span>' + timer.days + '</span>'  //put in clock element our time
						+ '<span>' + timer.hours + '</span>'
						+ '<span>' + timer.minutes + '</span>'
						+ '<span>' + timer.seconds + '</span>';

		var spans = clock.getElementsByTagName("span");
		animateClock(spans[3]);
		if (timer.seconds == 59) animateClock(spans[2]);
		if (timer.minutes == 59 && timer.seconds == 59) animateClock(spans[1]);
		if (timer.hours == 23 && timer.minutes == 59 && timer.seconds == 59) animateClock(spans[0]);
		
	if (timer.total < 1) {
		clearInterval(timerInterval);
		clock.innerHTML = '<span>0</span><span>0</span><span>0</span><span>0</span>';
	}					

	}, 1000);
};
