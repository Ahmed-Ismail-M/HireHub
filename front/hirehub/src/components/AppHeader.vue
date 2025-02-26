<template>
  <header>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <router-link class="navbar-brand" to="/">Employee Portal</router-link>
        <div class="navbar-nav">
          <router-link class="nav-link" to="/">Home</router-link>
          <router-link class="nav-link" to="/companies">Companies</router-link>
          <router-link class="nav-link" to="/departments">Departments</router-link>
          <router-link class="nav-link" to="/employees">Employees</router-link>
          <router-link class="nav-link" to="/login">Login</router-link>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
// No script needed for static header
</script>
