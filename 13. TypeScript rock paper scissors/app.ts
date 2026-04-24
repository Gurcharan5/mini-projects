import PromptSync from 'prompt-sync';
const prompt = PromptSync();

const moves = ['Rock', 'Paper', 'Scissors'];

function getRandomInt(max: number){
    return Math.floor(Math.random() * max);
}

function checkMoves(computerMove: string, playerMove: string){

    console.log("The computer chose: " + computerMove);

    if (computerMove == "Rock" && playerMove == "Scissors"){
        console.log('You lose');
    } else if (computerMove == "Rock" && playerMove == "Rock"){
        console.log("It's a draw");
    } else if (computerMove == "Paper" && playerMove == "Rock"){
        console.log('You lose');
    } else if (computerMove == "Paper" && playerMove == "Paper"){
        console.log("It's a draw");
    } else if (computerMove == "Scissors" && playerMove == "Paper"){
        console.log('You lose');
    } else if (computerMove == "Scissors" && playerMove == "Scissors"){
        console.log("It's a draw");
    } else {
        console.log("You win!");
    }

    playGame();
}

function rockPaperScissors(){
    var computerMove = moves[getRandomInt(moves.length)];

    console.log('Are you playing Rock, Paper or Scissors?')
    var userMove = prompt("");

    if (userMove == 'Rock'){
        checkMoves(computerMove, userMove);
    } else if (userMove == 'Paper'){
        checkMoves(computerMove, userMove);
    } else if (userMove == 'Scissors'){
        checkMoves(computerMove, userMove);
    } else {
        console.log("You did not give a valid play!");
        rockPaperScissors();
    }
}

function playGame(){
    console.log('Are you ready to play?');
    console.log('Yes or No');
    var userInput = prompt("");

    if (userInput == 'Yes'){
        rockPaperScissors();
    } else if (userInput == 'No'){
        console.log("Thanks for playing!");
    } else {
        console.log("You did not give a valid input");
        console.log("Please reply with Yes or No");
        playGame();
    }
}

playGame();