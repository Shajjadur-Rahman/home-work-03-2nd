$(document).ready(function () {
  $(".js__services_section").waypoint(function (direction) {
    if (direction == "down") {
      $(".header").addClass("sticky");
    } else {
      $(".header").removeClass("sticky");
    }
  });

  //Counter up
  $(".counter").counterUp({
    delay: 20,
    time: 1500,
  });
  $(".banner_bg").ripples({
    dropRadius: 10,
    perturbance: 0.01,
  });
  $(".wripple").ripples({
    dropRadius: 12,
    perturbance: 0.5,
  });
  $(".wripple").ripples({
    dropRadius: 12,
    perturbance: 0.5,
  });
  $(".my_info").ripples({
    dropRadius: 12,
    perturbance: 0.5,
  });

  AOS.init();
  //slick slider

  $(".demo").slick({
    autoplay: true,
  });
});
// type.js

var typed = new Typed(".text1", {
  strings: [
    "Hello every one.....",
    "This is Mr.Shajjad .",
    "I'm full stack Python Developer !",
    "Thank you so much..... ",
    "for visiting my website",
    "And you can contact with me...",
    "for any kind of consultation..",
    "in 'python' programming and....",
    "Web design related topics !",
    "You can knock me at ",
    "any time .",
    "I'm dedicated and open minded",
    "for all",
    "And available 24/7 in online !",
    "Best of luck !",
    "Thanks again !",
  ],
  typeSpeed: 50,
  backSpeed: 10,
  loop: true,
});

// 3-d slider
var swiper = new Swiper(".swiper-container", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 80,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true,
  },
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  },
});
//mobile menu
function openNav() {
  var myNav = document.getElementById("myNav");
  myNav.style.width = "100%";
}
function closeNav() {
  var myNav = document.getElementById("myNav");
  myNav.style.width = "0%";
}
