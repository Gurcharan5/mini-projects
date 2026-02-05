function calculate(){
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operation = document.getElementById('operator').value;

    let result;

    if (operation == 'add'){
        result = parseFloat(num1) + parseFloat(num2);
    } else if (operation == 'subtract'){
        result = parseFloat(num1) - parseFloat(num2);
    } else if (operation == 'times'){
        result = parseFloat(num1) * parseFloat(num2);
    } else if (operation == 'divide'){
        result = parseFloat(num1) / parseFloat(num2);
    }

    alert("The answer is: " + result);
}