<template>
  <div>
    <input type="text" v-model="address" placeholder="Введите адрес">
    <button @click="geocodeAddress">Найти координаты</button>
    <div v-if="coordinates">
      Широта: {{ coordinates.latitude }}
      Долгота: {{ coordinates.longitude }}
    </div>
  </div>
</template>

<script>
import { geocode } from './geOps.js/main';

export default {
  data() {
    return {
      address: '',
      coordinates: null,
    };
  },
  methods: {
    async geocodeAddress() {
      try {
        const response = await geocode(this.address);
        this.coordinates = response.results[0].geometry.coordinates;
      } catch (error) {
        // Обработка ошибок
      }
    },
  },
};
</script>