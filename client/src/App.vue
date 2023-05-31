<template>
  <div>
    <iframe src="https://176.99.128.10/embed/10" width="597" height="337" frameborder="0"></iframe>
  </div>
  <div>
    <iframe src="https://176.99.128.10/embed/7" width="597" height="337" frameborder="0"></iframe>
  </div>
  <div>
    <iframe src="https://176.99.128.10/embed/1" width="597" height="337" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  // mounted() {
  //   this.startVideoStream();
  // },
  methods: {
    startVideoStream() {
      const socket = new WebSocket('ws://localhost:8000/video-stream');

      // Обработка полученных данных через WebSocket
      socket.onmessage = (event) => {
        const videoPlayer = this.$refs.videoPlayer;

        // Обновление src объекта videoPlayer для отображения видеопотока
        if (videoPlayer.src === '') {
          videoPlayer.srcObject = event.data;
        }
      };
    },
  },
};
</script>