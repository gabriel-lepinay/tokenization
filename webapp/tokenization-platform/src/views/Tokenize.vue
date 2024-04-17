<script setup>
  import { ref } from 'vue'

  const message = ref('')
  const token = ref('')
  const tokenHistory = ref([])
  const errorMessage = ref('')
  const tokenize = () => {
    errorMessage.value = ""

    if (!message.value) {
      errorMessage.value = "Message field cannot be empty"
      return
    }

    if (message.value.includes("/")) {
      errorMessage.value = "Message cannot contain '/'"
      return
    }

    if (message.value.length > 127) {
      errorMessage.value = "Message cannot be longer than 127 characters"
      return
    }

    fetch(`http://127.0.0.1:8000/api/tokenize/${message.value}`)
      .then(async response => {
        const data = await response.json()

        if (!response.ok) {
          const error = response.status + ' ' + response.statusText
          errorMessage.value = error
          return Promise.reject(error)
        }
        token.value = data.token
        tokenHistory.value.push(token.value)
      })
  }
</script>

<template>
  <main class="tokenizePage">
    <section class="card">
      <input v-model="message" placeholder="Enter your string to tokenize here" />
      <button @click="tokenize">Tokenize</button>
      <p v-if="{errorMessage}" class="errorMessage">{{ errorMessage }}</p>
    </section>
    <section class="resultCard">
      <h3>Token</h3>
      <p class="result">{{ token }}</p>
    </section>
  </main>
</template>


<style>
  .tokenizePage {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .tokenizePage .card {
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

  .tokenizePage input {
    border: none;
    border-bottom: 2px solid #000000;
    background-color: #EDEDED;
    width: 60%;
    margin-bottom: 15px;
  }

  .tokenizePage input:focus {
    outline: none;
  }

  .tokenizePage button {
    background-color: #EF8A17;
    color: #FFFFFF;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
  }

  .tokenizePage button:active {
    transform: scale(0.95);
  }

  .tokenizePage .errorMessage {
    color: #EF3717;
    font-size: 10px;
    font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: light;
  }

  .tokenizePage .resultCard {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 15px;
  }

  .tokenizePage h3 {
    font-size: 20px;
    margin: 0px 0px;
    font-family: Roboto,'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: bold;
    color: #000000;
  }

  .tokenizePage .result {
    background-color: #EDEDED;
    border-radius: 5px;
    padding: 10px 10px;
    width: 630px;
    height: 20px;
    text-align: center;
  }

</style>