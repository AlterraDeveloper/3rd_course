// document.ready(function() {
// 	'[data-toggle="toggle"]'.change(function(){
// 		this.parents().next('.hide').toggle();
// 	});
// });

const chkBoxes = document.querySelectorAll("input[type=checkbox]");
const rowsToHide = document.querySelectorAll('.hide');
rowsToHide.forEach(row =>{
    row.hidden = true;
})
for (let index = 0; index < chkBoxes.length; index++) {
    chkBoxes[index].addEventListener('change',e => {
        if(e.target.checked === true){
            rowsToHide[index].hidden = false;
        }else{
            rowsToHide[index].hidden = true;
        }
    });
}
