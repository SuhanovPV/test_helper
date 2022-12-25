function getInvisibleDiv(){
    var divs = document.querySelectorAll('.invisible');
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

function set_start_time(cur_div, prev_div) {
    var current_div_time = getDateTime(cur_div);
    var prev_end_time = getDateTime(prev_div)[1].value;

    console.log(prev_end_time);
    current_div_time[0].value = prev_end_time;

    var d = new Date(prev_end_time);
    d.setMinutes(d.getMinutes() + 5);
    d.setHours(d.getHours() + 3);
    current_div_time[1].value = d.toJSON().slice(0, 16);
}

function makeVisible(){
    var div = getInvisibleDiv();
    console.log(div);
    if (div) {
        var checkbox = getCheckBox(div);
        checkbox.checked = true;
        div.classList.remove('invisible');
        /*set_start_time(div, div.previousElementSibling);*/
    }
}