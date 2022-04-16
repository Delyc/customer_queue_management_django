

$(".disable-sound").on("click", (e) => {
  const state = localStorage.getItem("notify");
  console.log(state);
  if (!state) {
    localStorage.setItem("notify", false);
    $(".speaker-img").attr("src", "/static/muted.svg");
  } else if (state == "true") {
    localStorage.setItem("notify", false);
    $(".speaker-img").attr("src", "/static/muted.svg");
  } else if (state == "false") {
    localStorage.setItem("notify", true);
    $(".speaker-img").attr("src", "/static/speaker.png");
  }
});
