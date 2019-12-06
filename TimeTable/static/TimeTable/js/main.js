$('[data-toggle="datepicker"]').datepicker(); //datepicker newindex
//dropdown
let dropdown = $('#dropdownMenuButton');
let dropdownItem = $('.dropdown-item');
let a = $("#SearchID")
console.log(a);
dropdownItem.on('click', (event) => {
	// console.log(event);
	dropdown[0].textContent = event.currentTarget.innerText;
  console.log(event.currentTarget.getAttribute("value"));
  dropdown[0].value = event.currentTarget.getAttribute("value");
  // $("#SearchID").href = "/eventsList/" + event.currentTarget.value; getAttribute("class");
});
a.on("click", (event) => {
  // console.log(event);
  event.currentTarget.href = "/eventsList/" + dropdown[0].value
})