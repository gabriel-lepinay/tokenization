<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'

const apiStatus = ref(false)

fetch('http://127.0.0.1:8000/api/status')
  .then(async response => {
    const data = await response.json()

    if (!response.ok) {
      const error = response.status + ' ' + response.statusTextAPI
    }

    console.log("[API]: connected.")
    apiStatus.value = data.connected
  })
</script>

<template>
  <header class="webHeader">
      <nav>
        <RouterLink to="/" class="text">Tokenize</RouterLink>
        <RouterLink to="/detokenize" class="text">Detokenize</RouterLink>
      </nav>
      <section class="apiStatus">
        <p class="status" :class="{connected: apiStatus === true}">API status</p>
      </section>
  </header>
  <RouterView />
</template>

<style>

.webHeader {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.apiStatus {
  position: absolute;
  right: 0;
  margin-right: 30px;
  top: 0;
}

.status {
  font-size: 14px;
  font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: bold;
  color: #ef3717;
  text-decoration: none;
  border: 2px solid #ef3717;
  border-radius: 5px;
  padding: 5px 10px;
}

.connected {
  color: #14c004;
  border: 2px solid #14c004;
}

a.router-link-active {
  color: #EF8A17;
  border-bottom: 2px solid #EF8A17;
}

.text {
  font-size: 20px;
  font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: bold;
  color: #000000;
  text-decoration: none;
  margin-right: 30px;
}
</style>
