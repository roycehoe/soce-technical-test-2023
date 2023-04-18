<script setup lang="ts">
import {
  BodyComponent,
  currentBodyComponent,
} from "../composables/useBodyComponent";
import Admin from "../views/Admin/Index.vue";
import Shop from "../views/Shop.vue";
</script>

<template>
  <Shop v-if="currentBodyComponent === BodyComponent.Shop"></Shop>
  <Admin v-if="currentBodyComponent === BodyComponent.Admin"></Admin>
</template>
<style scoped></style>
