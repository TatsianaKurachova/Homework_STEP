const Days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"];

for (let i = 0; i < Days.length; i++) {
  if (Days[i] == "Суббота" || Days[i] == "Воскресенье") {
    document.write("<strong>" + Days[i] + "</strong><br>");
  } 
  else {
    document.write(Days[i] + "<br>");
  }
}