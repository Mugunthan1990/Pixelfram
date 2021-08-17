const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

@types/jquery
$('a#showvideo').click(function(e) {
    e.preventDefault();
    $('div#test').html('<iframe id="video" width="420" height="315" src="//www.youtube.com/embed/aS3DPglji0o?rel=0" frameborder="0" allowfullscreen></iframe>');
});
