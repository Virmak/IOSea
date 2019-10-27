var seaLevelZ = 0;
  var yearSpan;
  var firstSeaUpdate = true;
  window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('raiseButton').addEventListener('click', () => {
      movePlane(+0.01)
    });
    document.getElementById('downButton').addEventListener('click', () => {
      movePlane(-0.01)
    });

    setTimeout(() => {
      movePlane(-0.07);
      app.scene.mapLayers[3].opacity = 0.7
    }, 500);

    yearSpan = document.getElementById('yearVal');

  });

  function movePlane(val) {
    if (val < 0 && seaLevelZ <= -0.07) {
      return;
    }
    var mesh = app.scene.mapLayers[3].objectGroup;

    updateSeaLevel(val)
    mesh.position.z = seaLevelZ;

    app.scene.updateMatrixWorld();
    app.scene.requestRender();
  }

  function updateSeaLevel(val) {
    seaLevelZ = seaLevelZ + val;
    if (!firstSeaUpdate) {
      var coef = 1;
      if (val < 0) {
        coef = -1;
      }

      if (yearSpan.innerHTML == 2019 || yearSpan.innerHTML == 2300 && coef == -1) {
        yearSpan.innerHTML = +yearSpan.innerHTML + 81 * coef;
      } else {
        yearSpan.innerHTML = +yearSpan.innerHTML + 100 * coef
      }
    }  

    firstSeaUpdate = false;
  }

