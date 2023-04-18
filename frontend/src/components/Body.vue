<script setup lang="ts">
import {
  BodyComponent,
  currentBodyComponent,
} from "../composables/useBodyComponent";
import { client } from "../services";
// import Admin from "../views/Admin/Index.vue";
import Admin from "../views/Admin/Index.vue";
import Shop from "../views/Shop.vue";

async function test() {
  const response = await client.get("/items/");
  console.log(response);
}
</script>

<template>
  <Shop v-if="currentBodyComponent === BodyComponent.Shop"></Shop>
  <Admin v-if="currentBodyComponent === BodyComponent.Admin"></Admin>
  <button @click="test">CLICK ME</button>
</template>
<style scoped></style>
