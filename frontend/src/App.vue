<!-- <script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script> -->

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">主页</RouterLink>
        <RouterLink to="/community">灵感广场</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
  /* 这里可以添加一些样式让导航更好看 */
  header {
    line-height: 1.5;
    max-height: 100vh;
  }
  nav {
    width: 100%;
    font-size: 1rem;
    text-align: center;
    margin-top: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #ddd;
  }
  nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
    text-decoration: none;
    color: #2c3e50;
    transition: 0.3s;
  }
  nav a:first-of-type {
    border: 0;
  }
  nav a.router-link-exact-active {
    color: #42b983;
  }
</style>