function encrypt(text){
    let result = "";
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    let modifiedAlphabet = "qazwsxedcrfvtgbyhnujmikolp";

    for (i=0; i<text.length; i++){
        for (m=0; m<alphabet.length; m++){
            if (text[i] == " "){
                result += " ";
                break;
            } else  if (text[i] == alphabet[m]){
                result += modifiedAlphabet[m];
                break;
            }
        }
    }

    console.log("The encrypted text is: " + result);
    decrypt(result)
}

function decrypt(text){
    let orignal = "";
    let encrytedAlphabet = "qazwsxedcrfvtgbyhnujmikolp"
    let orignalAlphabet = "abcdefghijklmnopqrstuvwxyz"

    for (i=0; i < text.length; i++){
        for (m=0; m<encrytedAlphabet.length; m++){
            if (text[i] == " "){
                orignal += " ";
                break;
            } else if (text[i] == encrytedAlphabet[m]){
                orignal += orignalAlphabet[m];
            }
        }
    }

    console.log("The original text is: " + orignal)
}

encrypt("my favourite food is pizza");