jQuery.postJSON = function(url, args, callback) {
    //Send json encoded data to server and convert response into JS dict.
    //Note: requires the JSON utilities in the "pythonic_functions.js" file. 
    var json_string = json.dumps(args);
    var args_dict = {'json_string': json_string};
    $.ajax({url: url, data: $.param(args_dict), dataType: 'text', type: 'GET',
            success: function(response) {
		var json_string = response;
		var response_dict = json.loads(json_string);
		callback(response_dict);
	    }});
};

function apply_game_engine_response(response_dict)
{
    var game_state = response_dict['game_state'];
    var game_over_flag = response_dict['game_over_flag'];
    var game_winner = response_dict['game_winner'];

    $.each(game_state, function(index, value) {
        if(value == ' ') value = '&nbsp;'; // The actual html in the cell should be "&nbsp;", not " " because " " creates rendering issues.             
        $('#cell_' + index ).html(value);
    });
    if(game_over_flag == 1) // Using int flags here instead of Python's True/False bool type for python/JS compatibility.
    {
	$('#cover').show();
	if(game_winner == 'o') game_winner = 'Computer Won';
	if(game_winner == 'draw') game_winner = 'it was a draw';
	alert("Game Over: " + game_winner);
    }
}

$(document).ready(function() {
    $('.game_cell').click(function() {
        var cell_id = this.id;
	var clicked_cell_contents = $('#' + cell_id).html(); 
	if(clicked_cell_contents != 'x' && clicked_cell_contents != 'o')
	{
            $('#' + cell_id).html('x'); // Insert 'x' into the clicked cell.

	    var game_state = [];
	    $('.game_cell').each(function(index) {
		var cell_contents = $('#' + this.id).html();
		if(cell_contents == '&nbsp;') cell_contents = ' ';
		game_state.push(cell_contents);
	    });
	    $.postJSON('/game_engine/', game_state, apply_game_engine_response);
        }
    });
});
