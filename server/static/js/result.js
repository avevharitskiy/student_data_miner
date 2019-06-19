$(function() {
    model = $('#model')[0];
    model.style.width = window.innerWidth - 100;
    model.style.height = window.innerHeight - $('.header_block')[0].clientHeight - 100;
    svg_image = document.getElementsByTagName('svg')[0];
    svg_image.setAttribute('id','svg-id');
    svg_image.style = "display: inline; width: inherit; min-width: inherit; max-width: inherit; height: inherit; min-height: inherit; max-height: inherit;"
    panZoomInstance = svgPanZoom('#svg-id', {
      zoomEnabled: true,
      controlIconsEnabled: true,
      fit: true,
      center: true,
      minZoom: 0.01
    });

    // zoom out
    panZoomInstance.zoom(0.9)
  })