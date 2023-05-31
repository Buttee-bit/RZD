<template>
  <div class="app">
    <router-view></router-view>
  </div>

</template>

<script>

export default {
  name: 'App',

}
</script>

<style>
.app{
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
body {
  margin: 0;
}
</style>
