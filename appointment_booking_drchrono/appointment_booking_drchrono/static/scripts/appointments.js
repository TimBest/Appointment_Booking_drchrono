$("input[name='time_slots']").change(function(){
  $("#id_appointment_date").val($(this).val());
});

$(document).ready(function() {
  $(".rotate_table").each(function () {
      var $this = $(this);
      var newrows = [];
      $this.find("tr").each(function () {
          var i = 0;
          $(this).find("td,th").each(function () {
              i++;
              if (newrows[i] === undefined) {
                  newrows[i] = $("<tr></tr>");
              }
              newrows[i].append($(this));
          });
      });
      $this.find("tr").remove();
      $.each(newrows, function () {
          $this.append(this);
      });
  });
});
