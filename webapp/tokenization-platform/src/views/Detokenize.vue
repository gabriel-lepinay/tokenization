<script setup>
  import { ref } from 'vue'

  const token = ref('')
  const detokenizedMessage = ref('')
  const errorMessage = ref('')

  const detokenize = () => {
    if (!token.value) {
      errorMessage.value = "Token field cannot be empty"
      return
    }

    if (token.value.length != 64) {
      errorMessage.value = "Token invalid"
      return
    }

    fetch(`http://127.0.0.1:8000/api/untokenize/${token.value}`)
      .then(async response => {
        const data = await response.json()

        if (!response.ok) {
          const error = response.status + ' ' + response.statusText
          errorMessage.value = error
          return Promise.reject(error)
        }
        detokenizedMessage.value = data.data
      })
  }
</script>

<template>
  <main class="detokenizePage">
    <section class="card">
      <input v-model="token" placeholder="Enter your token here" />
      <button @click="detokenize">Detokenize</button>
      <p v-if="{errorMessage}" class="errorMessage">{{ errorMessage }}</p>
    </section>
    <section v-if="detokenizedMessage" class="result">
      <h3>Detokenized message</h3>
      <p>{{ detokenizedMessage }}</p>
    </section>
  </main>
</template>

<style>
  .detokenizePage {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .detokenizePage .card {
    width: 500px;
    height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 5%;
    background-color: #EDEDED;
    border-radius: 15px;
  }

  .detokenizePage input {
    border: none;
    border-bottom: 2px solid #000000;
    background-color: #EDEDED;
    width: 60%;
    margin-bottom: 15px;
  }

  .detokenizePage input:focus {
    outline: none;
  }

  .detokenizePage button {
    background-color: #EF8A17;
    color: #FFFFFF;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
  }

  .detokenizePage button:active {
    transform: scale(0.95);
  }

  .detokenizePage .errorMessage {
    font-size: 10px;
    font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: light;
    color: #EF3717;
  }

  .detokenizePage .result {
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .detokenizePage .result h3 {
    font-size: 20px;
    margin: 0px 0px;
    font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: bold;
    color: #000000;
  }

  .detokenizePage .result p {
    font-size: 16px;
    font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: light;
    color: #000000;
    padding: 20px 40px;
    background-color: #EDEDED;
    border-radius: 5px;
  }

</style>