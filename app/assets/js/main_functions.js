jQuery.postJSON = function(url, args, callback) {
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
    if(game_over_flag == 1)
    {
	alert("Game Over " + game_winner);
    }
    else
    {
	$.each(game_state, function(index, value) {
	    if(value == ' ') value = '&nbsp;';
	    $('#cell_' + index ).html(value);
	});
    }
}

$(document).ready(function() {
    $('.game_cell').click(function() {
        var cell_id = this.id;
	var clicked_cell_contents = $('#' + cell_id).html(); 
	if(clicked_cell_contents != 'x' && clicked_cell_contents != 'o')
	{
            $('#' + cell_id).html('x');

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