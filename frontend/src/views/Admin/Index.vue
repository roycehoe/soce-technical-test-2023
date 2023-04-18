<script setup lang="ts">
import { onBeforeMount } from "vue";
import { currentItems, useItems } from "../../composables/useItems";
import CurrentItemForm from "./CurrentItemForm.vue";
import NewItem from "./NewItemForm.vue";

const { updateCurrentItems } = useItems();

onBeforeMount(updateCurrentItems);
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex flex-wrap mx-24 text-center current-store--group">
      <CurrentItemForm
        v-for="item in currentItems"
        :item="item"
        :key="item.id"
      ></CurrentItemForm>
      <NewItem></NewItem>
    </div>
  </div>
</template>
<style scoped></style>
