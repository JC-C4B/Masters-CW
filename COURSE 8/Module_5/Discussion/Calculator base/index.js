let display = document.getElementById('display');
let currentValue = ''; 
let result = ''; 

let buttons = Array.from(document.getElementsByClassName('button'));

buttons.map(button => {
    button.addEventListener('click', (e) => {
        switch (e.target.innerText) {
            case 'C':
                display.innerText = '';
                currentValue = '';
                result = '';
                break;
            case '=':
                try {
                    display.innerText = eval(currentValue);
                    result = display.innerText;
                } catch {
                    display.innerText = "Error";
                }
                break;
            case '←':
                if (display.innerText) {
                    display.innerText = display.innerText.slice(0, -1);
                    currentValue = display.innerText;
                }
                break;
            case '+/-':
                if (display.innerText !== '') {
                    let x = parseFloat(display.innerText);
                    display.innerText = (-x).toString();
                    currentValue = display.innerText;
                }
                break;
            case '%':
                if (display.innerText) {
                    let x = parseFloat(display.innerText);
                    display.innerText = (x / 100).toString();
                    currentValue = display.innerText;
                    result = display.innerText;
                }
                break;
            default:
                display.innerText += e.target.innerText;
                currentValue = display.innerText;
        }
    });
});
