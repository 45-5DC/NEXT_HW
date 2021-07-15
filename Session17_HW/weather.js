const input = document.querySelector("#city");
const button = document.querySelector("#submit");
const weatherBox = document.querySelector("#box_wrapper");

const API_KEY = "dcb31ba5e778d86d67af537a9338f732";

button.addEventListener("click", async () => {
  //input의 값을 가져와서 도시이름으로 url에 넣는다.
  const city = input.value;

  try {
    const res = await axios.get(
      `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${API_KEY}`
    );
    console.log(res);

    weatherBox.innerHTML = ''

    for (let i = 2; i < 7; i++) {
    //res에서 원하는 값 가져오기
    const { main, description, icon } = res.data.list[i].weather[0];
    const temp = Math.round(res.data.list[i].main.temp - 273.15);
    const name = res.data.city.name;
    const time = res.data.list[i].dt_txt;
    
    //사용자에게 보여주기
    weatherBox.innerHTML += `
      <div id="weatherBox">
      <div class="name">${name}</div>
      <div class="time">${time}</div>
      <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
      <div class="main">${main}</div>
      <div class="description">${description}</div>
      <div class="temp">${temp}°C</div>
      </div>
    `};
  } catch (error) {
    console.log(error);
  }
});
