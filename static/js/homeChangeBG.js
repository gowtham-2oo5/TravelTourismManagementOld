function changeBG() {
  const btn = document.querySelector("#bgChange-btn");
  if (document.body.style.backgroundColor == "aliceblue") {
    document.body.style.backgroundColor = "#0f0f0f";
    document.body.style.color = "#ffffff";
    btn.style.backgroundColor = "#ffffff";
    btn.style.color = "#0f0f0f";
  } else {
    document.body.style.backgroundColor = "aliceblue";
    document.body.style.color = "#000000";
    btn.style.backgroundColor = "#000000";
    btn.style.color = "#ffffff";
  }
}
