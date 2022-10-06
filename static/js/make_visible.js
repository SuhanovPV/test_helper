function getInvisibleDiv(){
    divs = document.querySelectorAll('.invisible');
    if (divs.length > 0) {
        return divs[0]
    }
    return null
}

function getCheckBox(div) {
    return div.querySelector("input[type='checkbox']")
}

function makeVisible(){
    div = getInvisibleDiv();
    if (div) {
        checkbox = getCheckBox(div);
        checkbox.checked = true;
        div.classList.remove('invisible');
    }
}