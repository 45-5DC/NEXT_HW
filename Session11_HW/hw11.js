// 과제 1
const getRandomHexaColor = () => {
    const hexa = '0123456789abcdef';
    let color = "#";
    for (let i=0; i<6; i++) {
        color += hexa[Math.floor(Math.random()*16)];
    };
    return color;
};

setInterval(() => {
    document.querySelector('body').style.backgroundColor =
        getRandomHexaColor();
}, 100);


// 과제 2
const clockContent = document.querySelector('.now');

const getCurrentTime = () => {
    const date = new Date();

    let year = date.getFullYear();
    let month = date.getMonth()+1;
    let day = date.getDate();
    let hour = date.getHours();
    let minute = date.getMinutes();
    let second = date.getSeconds();

    month = (month < 10) ? ('0' + month) : (month);
    day = (day < 10) ? ('0' + day) : (day);
    hour = (hour < 10) ? ('0' + hour) : (hour);
    minute = (minute < 10) ? ('0' + minute) : (minute);
    second = (second < 10) ? ('0' + second) : (second);

    clockContent.innerText = `${year}년 ${month}월 ${day}일 ${hour}시 ${minute}분 ${second}초`;
};

const initClock = () => {
    getCurrentTime();
    setInterval(getCurrentTime, 1000);
};

initClock();