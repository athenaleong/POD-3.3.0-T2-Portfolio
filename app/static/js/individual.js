new Glider(document.querySelector('.glider'), {
    slidesToShow: 3,
    dots: '#dots',
    arrows: {
        prev: '.glider-prev',
        next: '.glider-next'
}
});

$(".panel").click(function() {
    window.location = $(this).data("location");
  });


