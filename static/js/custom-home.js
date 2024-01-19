// add functionality for the all tables row text fields to have good view

let elementsArray = document.querySelectorAll(".textinput");

elementsArray.forEach(function (elem) {
    elem.addEventListener("input", function () {
        let requiredId = elem.id
        if (elem.value.length > 30) {
            document.getElementById('s-' + requiredId).innerHTML = "مقدار بیشتر از ۳۰ کارکتر ذخیره نخواهد شد ."
        }
        else {
            document.getElementById('s-' + requiredId).innerHTML = ''
        }
    });
});

//--------------------------------------------------------------------------------------------------------------------//
