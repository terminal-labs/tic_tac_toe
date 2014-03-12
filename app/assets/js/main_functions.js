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
    alert(response_dict);
}

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

	$.postJSON('/game_engine/', game_state, apply_game_engine_response);
    });
});