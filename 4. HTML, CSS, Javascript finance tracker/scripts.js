function add_income(){
    const description = document.getElementById("inc-desc").value;
    const number = document.getElementById("inc-num").value;
    const current_balance_txt = document.getElementById("current-balance").textContent;
    const current_balance_val = parseFloat(current_balance_txt);
    const transactions = document.getElementById("transaction-history");

    const li = document.createElement("li");
    li.innerText = description + ": +" + number;
    transactions.append(li);

    let new_balance = current_balance_val;
    new_balance += parseFloat(number);

    document.getElementById("current-balance").innerHTML = new_balance;
}

function add_expense(){
    const description = document.getElementById("exp-desc").value;
    const number = document.getElementById("exp-num").value;
    const current_balance_txt = document.getElementById("current-balance").textContent;
    const current_balance_val = parseFloat(current_balance_txt);
    const transactions = document.getElementById("transaction-history");

    const li = document.createElement("li");
    li.innerText = description + ": -" + number;
    transactions.append(li);

    let new_balance = current_balance_val;
    new_balance -= parseFloat(number);

    if (new_balance < 0){
        alert("You have a netagive balance!");
    }

    document.getElementById("current-balance").innerHTML = new_balance;
}