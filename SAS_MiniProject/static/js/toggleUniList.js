document.getElementById("userUniStaff").addEventListener("change", Display_UniOption);
document.getElementById("userStudent").addEventListener("change", Display_UniOption);

function Display_UniOption(){
    var displayOpt = document.getElementById("UniAccount");
    var radioOpt = document.getElementById("userUniStaff");

    if (radioOpt.checked){
        displayOpt.style.display = "block";
    }
    else{
        displayOpt.style.display = "none";
    }
}