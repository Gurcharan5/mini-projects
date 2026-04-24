function getRandomInt(max){
    return Math.floor(Math.random() * max);
}

function recommendWorkout(area){
    const workouts = {
    "arms":["pushups", "tricep dips", "up downs", "diamond pushups", "wide arm pushups"],
    "back": ["w pulldowns", "w raises", "over under"],
    "legs": ["squats", "leg raises", "lunges"],
    "abs": ["situps", "crunches"]
    }

    let output = "";

    if (area == "1"){
        output = workouts.arms[getRandomInt(workouts.arms.length)];
    } else if (area == "2") {
        output = workouts.back[getRandomInt(workouts.back.length)];
    } else if (area == "3"){
        output = workouts.legs[getRandomInt(workouts.legs.length)];
    } else if (area == "4"){
        output = workouts.abs[getRandomInt(workouts.abs.length)];
    } else {
        output = "You did not choose a valid workout area!";
    }

    document.getElementById("workoutToDo").innerHTML = output;
}

function countdown(maxTime){
    let timeLeft = Number(maxTime);
    const timer = document.getElementById("timer");

    timer.innerHTML = timeLeft;

    const interval = setInterval(() => {
        timeLeft --;
        timer.innerHTML = timeLeft;

        if (timeLeft <=0){
            clearInterval(interval);
            timer.innerHTML = "Time is over";
        }
    }, 1000)
}