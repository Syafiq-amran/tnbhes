

// ######################################################## ajax post get ########################################
$(document).ready(function(){
  $.ajax({
      url: 'http://127.0.0.1:8000/logs_list/',
      method: "GET",
      dataType: "json",
      success: function(data) {
          $("#myTable").dataTable({
          data:data,
          dom: "<'row'<'col-sm-4 pt-2'l><'col-sm-4 pt-2'><'col-sm-4'f>>"
          + "<'row'<'col-sm-4 pt-2'><'col-sm-6 pt-2'><'col-sm-2 pt-2 pl-4'B>>"
          + "<'row'<'col-sm-12 pt-2'tr>>"
          + "<'row'<'col-sm-6 pt-2'i><'col-sm-6 color-blue pt-3'p>>",
          searching: false,
          sort: false,
          columns: [
                  {'data': 'eventdatetime'},
                  {'data': 'eventname'},
                  // {'data': 'description'},
        ]
      })
    }
  })
})
$(document).ready(function(){ 
  $("#postget").dataTable();
})

$(document).ready(function(){
  var list = {};
  getlist();
  // $("#postget").dataTable();
$("#addButton").click(function(){
  // list.id = $("#txtid").val();
  // list.eventdatetime = $("#txtdatetime").val();
  list.eventname = $("#txtname").val();
  list.description = $("#txtdesc").val();
  // list.filepathname = $("#txtpath").val();
  list.transfduration = $("#txtduration").val();
  list.fromhost = $("#txtfrom").val();
  list.tohost = $("#txtto").val();
  list.comments = $("#txtcomment").val();
  var listObj = JSON.stringify(list);
  $.ajax({
  url: "http://127.0.0.1:8000/logs_list/",
  method: 'POST',
  data: listObj,
  contentType: 'application/json; charset=utf-8',
  success: function(){
    alert("add successfully");
    getlist();
  },
  error: function(error){
    alert('error');
  }
})
})
})

function getlist(){
$.ajax({
  url: "http://127.0.0.1:8000/logs_list/",
  method: "GET",
  dataType: 'json',
  success: function(data){
    $("#postget").dataTable({
      data:data,
      // columnDefs: [ {
      //   targets: 1,
      //   render: $.fn.dataTable.render.moment( 'X', 'Do MMM YY' ),
      // } ],
      dom: "<'row'<'col-sm-4 pt-2'l><'col-sm-4 pt-2'><'col-sm-4'f>>"
      + "<'row'<'col-sm-4 pt-2'><'col-sm-6 pt-2'><'col-sm-2 pt-2 pl-4'B>>"
      + "<'row'<'col-sm-12 pt-2'tr>>"
      + "<'row'<'col-sm-6 pt-2'i><'col-sm-6 color-blue pt-3'p>>",
      searching: false,
      sort: false,
      columns: [
        {'data': 'eventdatetime'},
        {'data': 'eventname'},
        {'data': 'description'},
        {'data': 'transfduration'},
        {'data': 'fromhost'},
        {'data': 'tohost'},
        {'data': 'comments'},
        // {'data': 'description'},
]
  })
  
    var tablebody = $('#postget tbody');
    tablebody.empty();
    $(data).each(function(index, element){
      tablebody.append('<tr><td>'+ element.id + 
      '</td><td>' + element.eventdatetime + 
      '</td><td>' + element.eventname + 
      '</td><td>' + element.description + 
      // '</td><td>' + element.filepathname + 
      '</td><td>' + element.transfduration + 
      '</td><td>' + element.fromhost + 
      '</td><td>' + element.tohost + 
      '</td><td>' + element.comments + 
      '</td></tr>');
    })
  },
  error: function(error){
    alert('error');
  }
})
}



$(document).ready(function () {
  $('#table').DataTable({
      "order": [[2, "desc"]],
      dom: "<'row'<'col-sm-4 pt-2'l><'col-sm-4 pt-2'><'col-sm-4'f>>"
          + "<'row'<'col-sm-4 pt-2'><'col-sm-6 pt-2'><'col-sm-2 pt-2 pl-4'B>>"
          + "<'row'<'col-sm-12 pt-2'tr>>"
          + "<'row'<'col-sm-6 pt-2'i><'col-sm-6 color-blue pt-3'p>>",

      // stateSave: true,
      buttons: [
          {
              extend: 'colvis',
              postfixButtons: ['colvisRestore'],
              sButtonClass: "text-right"
          }
      ],
      paging: true,
      // "columnDefs": [
      //     { "width": "8em", "targets": 0 },
      //     { "width": "8em", "targets": 5 },
      //     { "width": "2em", "targets": 7 }
      // ],

      language: {
          sLengthMenu: "SHOW _MENU_",
          searchPlaceholder: "Search",
          search: "",
      }


  });
});

var toggler = document.getElementsByClassName("carett");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function () {
      this.parentElement.querySelector(".nested").classList.toggle("active");
      this.classList.toggle("carett-down");
  });
}