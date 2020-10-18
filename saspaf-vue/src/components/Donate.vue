<template>
  <div id="donate">
    <div id="donate-content">
      <h1>Pay it forward.</h1>
      <br />
      <p>
        Your generous, tax-deductible donation will be used to support our
        services and effort to make a difference in the lives of single parents.
      </p>
      <br />
      <button class="button" id="donate-btn">DONATE NOW</button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Donate',
  components: {},
}
</script>

<style scoped>
#donate {
  display: flex;
  justify-content: center;
  background-color: var(--third-color);
  height: 30vh;
  width: 100%;
}

#donate-content {
  text-align: center;
  margin-top: 3vh;
  width: 45vw;
}

#donate-content h1 {
  font-size: 2rem;
  font-weight: 1000;
}

#donate-content p {
  font-size: 1.2rem;
}

#donate-btn {
  margin-top: 1vh;
  height: 4.5vh;
  width: 8vw;
  border-radius: 30px;
  border: none;
  color: white;
  background: var(--secondary-bg-color);
  box-shadow: 0 0 20px #14e67d;
  font-size: 1rem;
  font-weight: 1000;
}
</style>
