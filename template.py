partOne= '<!DOCTYPE html> \
<html> \
<head> \
<meta name="viewport" content="width=device-width, initial-scale=1"> \
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"> \
<style> \
body { \
  font-family: "Lato", sans-serif; \
} \
.topnav { \
  overflow: hidden; \
  background-color: #097ef2; \
} \
.topnav { \
  overflow: hidden; \
  background-color: #097ef2; \
} \
.topnav a { \
  float: right; \
/*  color: #ff3300; */ \
    color: #eaf2fa; \
  text-align: center; \
  padding: 14px 16px; \
  text-decoration: none; \
  font-size: 17px; \
} \
.topnav a:hover { \
  background-color: #ddd; \
  color: ff3300; \
} \
.topnav a.active { \
  background-color: #4CAF50; \
  color: #ff3300; \
} \
.topnav-right { \
  float: right; \
} \
/* Fixed sidenav, full height */ \
.sidenav { \
  height: 100%; \
  width: 200px; \
  position: fixed; \
  z-index: 1; \
  top: 0; \
  left: 0; \
  background-color: #097ef2; \
  overflow-x: hidden; \
  padding-top: 20px; \
} \
/* Style the sidenav links and the dropdown button */ \
.sidenav a, .dropdown-btn { \
  padding: 6px 8px 6px 16px; \
  text-decoration: none; \
  font-size: 20px; \
  color: #eaf2fa; \
  display: block; \
  border: none; \
  background: none; \
  width: 100%; \
  text-align: left; \
  cursor: pointer; \
  outline: none; \
} \
/* On mouse-over */ \
.sidenav a:hover, .dropdown-btn:hover { \
  color: #f1f1f1; \
} \
/* Main content */ \
.main { \
  margin-left: 200px; /* Same as the width of the sidenav */ \
  font-size: 20px; /* Increased text to enable scrolling */ \
  padding: 0px 10px; \
} \
/* Add an active class to the active dropdown button */ \
.active { \
  background-color: green; \
  color: white; \
} \
/* Dropdown container (hidden by default). Optional: add a lighter background color and some left padding to change the design of the dropdown content */ \
.dropdown-container { \
  display: none; \
  background-color: #262626; \
  padding-left: 8px; \
} \
/* Optional: Style the caret down icon */ \
.fa-caret-down { \
  float: right; \
  padding-right: 8px; \
} \
/* Some media queries for responsiveness */ \
@media screen and (max-height: 450px) { \
  .sidenav {padding-top: 15px;} \
  .sidenav a {font-size: 18px;} \
} \
table, th, td { \
  border: 1px solid black; \
  border-collapse: collapse; \
} \
th, td { \
  padding: 15px; \
  text-align: left; \
} \
table#t01 { \
  background-color: #c3ddf7; \
}\
</style> \
</head>'

partTwo= '<body> \
<div class="topnav"> \
  <div class="topnav-right"> \
    <a  href="/iot/logout">  Logout</a> \
    <a> Logged in: <B> uSeRnAmE </B> </a>   \
    <a  href="#search">Search</a> \
  </div> \
</div> \
<div class="sidenav"> \
  <a href="#about"><B><U>Main Menu</U></B></a> \
  <button class="dropdown-btn">Devices  \
    <i class="fa fa-caret-down"></i> \
  </button> \
  <div class="dropdown-container"> \
    <a href="/iot/devices"> -List Devices</a> \
    <a href="#"> -Add devices</a> \
    <a href="#"> -Delete Devices</a> \
  </div> \
  <button class="dropdown-btn">Analytics  \
    <i class="fa fa-caret-down"></i> \
  </button> \
  <div class="dropdown-container"> \
    <a href="/iot/devices">Summary</a> \
    <a href="#"> Anomaly Detection</a> \
    <a href="#">Custom</a> \
  </div> \
  <button class="dropdown-btn">User Management \
    <i class="fa fa-caret-down"></i> \
  </button> \
  <div class="dropdown-container"> \
    <a href="/iot/ListUsers"> -List Users</a> \
    <a href="#"> -Add Users</a> \
    <a href="#"> -Delete Users</a> \
  </div>  \
  <a href="#clients">Platfrom Security</a> \
  <a href="#about">About</a> \
</div>' 

mainSection = '<div class="main"> \
  <h2>Sidebar Dropdown</h2> \
  <p>Click on the dropdown button to open the dropdown menu inside the side navigation.</p> \
  <p>This sidebar is of full height (100%) and always shown.</p> \
  <p>Some random text..</p> \
</div>'

partThree = '<script>\
/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */\
var dropdown = document.getElementsByClassName("dropdown-btn");\
var i;\
for (i = 0; i < dropdown.length; i++) {\
  dropdown[i].addEventListener("click", function() {\
  this.classList.toggle("active");\
  var dropdownContent = this.nextElementSibling;\
  if (dropdownContent.style.display === "block") {\
  dropdownContent.style.display = "none";\
  } else {\
  dropdownContent.style.display = "block";\
  }\
  });\
}\
</script>\
</body>\
</html> '
