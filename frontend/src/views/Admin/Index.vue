<script setup lang="ts">
import { onBeforeMount } from "vue";
import { useItem } from "../../composables/useItem";
import { currentItems, useItems } from "../../composables/useItems";
import CurrentItemForm from "./CurrentItemForm.vue";
import NewItem from "./NewItemForm.vue";

const { getItems, updateCurrentItems } = useItems();
const { createItem, updateItem, deleteItem, isLoading } = useItem();

onBeforeMount(updateCurrentItems);
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex flex-wrap mx-24 text-center current-store--group">
      <CurrentItemForm
        v-for="item in currentItems"
        class="w-96 m-6 curent-store--cards"
        :key="item.id"
        :item="item"
      ></CurrentItemForm>
      <NewItem></NewItem>
    </div>
  </div>
</template>
<style scoped></style>
