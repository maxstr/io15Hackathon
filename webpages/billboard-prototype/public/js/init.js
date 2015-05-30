// retina images
var retinaLoad = function(){
  var images = document.querySelectorAll("img[data-1x]");
  if(window.devicePixelRatio == 2){
    Array.prototype.forEach.call(images, function(el, i){
      var src = el.getAttribute("data-2x");
      el.setAttribute("src",src);
    });
  }else{
    Array.prototype.forEach.call(images, function(el, i){
      var src = el.getAttribute("data-1x");
      el.setAttribute("src", src);
    });
  }
}();
var mobileinit = (function() {
  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    console.log("Mobile Restrictions");
    var mobileBreaks = (function(){
      var cell = document.getElementsByTagName("br");
      var length = cell.length;

      for(var i = 0; i < length; i++){
        cell[0].parentNode.removeChild(cell[0]);
      }
    })();
  }
})();