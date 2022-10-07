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

function getDateTimeStart(div) {
    return div.querySelector("input[type='datetime-local']")
}

function getDateTimeEnd(div) {
    return div.querySelectorAll("input[type='datetime-local']")[1]
}

// TODO: Изменить на получение старта и конца передачи для текущего и следущего дива, и заменой времени для них
function set_start_time(cur_div, prev_div) {
    prev_end_time = getDateTimeEnd(prev_div)
    start_time = getDateTimeStart(cur_div);
    start_time.value = prev_end_time.value
}

function makeVisible(){
    div = getInvisibleDiv();
    if (div) {
        checkbox = getCheckBox(div);
        checkbox.checked = true;
        set_start_time(div, div.previousElementSibling);
        div.classList.remove('invisible');
    }
}