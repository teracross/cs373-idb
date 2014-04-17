function drawPieChart(target, list){
var t;
function size(animate){
  if (animate == undefined){
    animate = false;
  }
  clearTimeout(t);
  t = setTimeout(function(){
    $("canvas").each(function(i,el){
      $(el).attr({
        "width":$(el).parent().width(),
        "height":$(el).parent().outerHeight()
      });
    });
    redraw(animate);
    var m = 0;
    $(".widget").height("");
    $(".widget").each(function(i,el){ m = Math.max(m,$(el).height()); });
    $(".widget").height(m);
  }, 30);
}
$(window).on('resize', function(){ size(false); });
function redraw(animation){
  var options = {};
  if (!animation){
    options.animation = false;
  } else {
    options.animation = true;
  }
    //Get context with jQuery - using jQuery's .get() method.
    var ctx = $("#"+target).get(0).getContext("2d");
    var data =
    [
      {
        value: list.0.count,
        color:"#F38630"
      },
      {
        value : list.1.count,
        color : "#E0E4CC"
      },
      {
        value : list.2.count,
        color : "#69D2E7"
      }
    ]
      new Chart(ctx).Pie(data, options);
  }
size(true);
    };