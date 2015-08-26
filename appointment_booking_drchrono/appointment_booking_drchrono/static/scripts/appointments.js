// Add datepicker
$("input[id='id_date_of_birth']").fdatepicker();

// copies table data into appointment_date field TODO remove this and just use time_slots
$("input[name='time_slots']").change(function(){
  $("#id_appointment_date").val($(this).val());
});

// Allows for a fixedheader on the table
$('.fixed-header').floatThead();
