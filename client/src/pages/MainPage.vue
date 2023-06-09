<template>
<div class="main-page">
    <Header_RZD/>
    <div class="wrapper">
        <div ref="map" class="map"></div>
    </div>
    <div class="log-info">
        блалаблаб
        <dif class="left-side">

        </dif>
        <div class="right-side">
          <video ref="videoPlayer" controls autoplay></video>
        </div>
    </div>
</div>

</template>


<script>
import Header_RZD from '../components/Header_RZD.vue';
import 'ol/ol.css';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
export default{
    components:{
        Header_RZD
    },
    mounted() {
  this.initMap();
  this.loadVideoStream();
},
    methods: {
      loadVideoStream() {
      const videoElement = this.$refs.videoPlayer;
      const videoUrl = "http://localhost:8000/video-stream"; // Update with your FastAPI server URL

      videoElement.src = videoUrl;
    },
    initMap() {
      const map = new Map({
        target: this.$refs.map,
        layers: [
          new TileLayer({
            source: new OSM()
          })
        ],
        view: new View({
          center: [0, 0],
          zoom: 2
        }),
      });
      
      // Создание метки
      const marker = new Map.Feature({
        geometry: new Map.geom.Point([0, 0]),
        name: 'Моя метка'
      });
      
      // Стиль метки
      const style = new Map.style.Style({
        image: new Map.style.Icon({
          src: 'path/to/icon.png' // Путь к изображению иконки метки
        })
      });
      
      marker.setStyle(style);
      
      // Создание векторного слоя для метки
      const vectorLayer = new Map.layer.Vector({
        source: new Map.source.Vector({
          features: [marker]
        })
      });
      map.addLayer(vectorLayer);
    },
  },
  
};
</script>



<style>
.wrapper{
  margin-top: 1%;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: center
}
.map {
  width: 90%;  
  height: 500px; /* Измените высоту по своему усмотрению */
}
.main-page {
  flex: 1;
}
.content {
  /* Стили для основного контента страницы */
  margin-bottom: 60px; /* высота футера */
}
.log-info{
    align-self: flex-end;
}
</style>