
// ****************************************************************************
// Functions that could be implemented to the script:
// Andy Fischer      info@Andyland.info
// ****************************************************************************

function FrontPanel() { }
var MyController = {};
var bShiftPressed = false;

MyController.init = function () {


	//----Zum Start das Item mit Playlists aufklappen
	engine.setValue("[Library]", "MoveDown", 1);
	engine.setValue("[Library]", "MoveDown", 1);
	//engine.setValue("[Library]", "GoToItem", 1);
	engine.setValue("[Library]", "MoveRight", 1);

};

MyController.shutdown = function () {

};

MyController.expandView = function (midichan, control, value, status, group) {
	//print(x)
	//engine.setValue("[Library]", "GoToItem", 1);
	engine.setValue("[Library]", "MoveRight", 1);
}

MyController.toggleSort_Artist = function () {
	engine.setValue("[Library]", "sort_column_toggle", 1);
}

MyController.toggleSort_Title = function () {
	engine.setValue("[Library]", "sort_column_toggle", 2);
}

MyController.toggleSort_Rating = function () {
	engine.setValue("[Library]", "sort_column_toggle", 19);
}

MyController.toggleSort_BPM = function () {
	engine.setValue("[Library]", "sort_column_toggle", 15);
}

MyController.rotateEncoder = function (midichan, control, value, status, group) {
	iStepSize = 1;
	if (bShiftPressed) {
		iStepSize = 15;
	}

	if (value > 63) {
		iStepSize = iStepSize * (-1);
	}

	engine.setValue("[Library]", "MoveVertical", iStepSize);
}

MyController.toggleShift = function (midichan, control, value, status, group) {

	if (value == 0) {
		bShiftPressed = false;
	} else {
		bShiftPressed = true;
	}

}