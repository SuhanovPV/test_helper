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

function getDateTime(div) {
    return div.querySelectorAll("input[type='datetime-local']")
}

// TODO: Изменить на получение старта и конца передачи для текущего и следущего дива, и заменой времени для них
function set_start_time(cur_div, prev_div) {
    current_div_time = getDateTime(cur_div);
    prev_end_time = getDateTime(prev_div)[1].value;

    current_div_time[0].value = prev_end_time;

    date = new Date(prev_end_time);
    date.setMinutes(date.getMinutes() + 5);

    current_div_time[1].value = date.toLocaleDateString();

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