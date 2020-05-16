/***********************************************
Responsive navigation
************************************************/
function openNav() {
	var show_nav_bar = document.getElementById("profile-nav");
	show_nav_bar.style.display = "flex";
	show_nav_bar.style.background = "#333";
				
	var hide_icon_menu = document.getElementById("icon-menu");
	hide_icon_menu.style.display = "none";
}

function closeNav() {
	var hide_nav_bar = document.getElementById("profile-nav");
	hide_nav_bar.style.display = "none";

	var show_icon_menu = document.getElementById("icon-menu");
	show_icon_menu.style.display = "flex";
}

/** Toggle on click event **/
document.querySelector(".icon-menu").addEventListener("click", openNav);
document.querySelector(".close-menu").addEventListener("click", closeNav);

