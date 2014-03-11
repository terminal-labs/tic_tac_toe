$(document).ready(function() {
    $('.game_cell').click(function() {
        cell_id = this.id;
        $('#' + cell_id).html('x');

	var game_state = [];
	$(".game_cell").each(function(index) {
	    var cell_contents = $('#' + this.id).html();
	    if(cell_contents == '&nbsp;') cell_contents = ' ';
	    game_state.push(cell_contents);
	});
    });
});