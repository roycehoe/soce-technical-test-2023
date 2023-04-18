<script setup lang="ts">
// import { onBeforeMount } from "vue";

import { ShopItemIn, useItem } from "../../composables/useItem";
import { useItems } from "../../composables/useItems";
import { DEFAULT_PRICE_DECIMAL_PLACES } from "../../constants";

const { getItems, updateCurrentItems } = useItems();
const { createItem, updateItem, deleteItem, isLoading } = useItem();
const { item } = defineProps<{ item: ShopItemIn }>();

// onBeforeMount(updateCurrentItems);
</script>

<template>
  <div class="card bg-base-100 shadow-xl">
    <div class="card-body">
      <input
        type="text"
        placeholder="Name"
        class="input input-ghost p-0 card-title text-center"
        :value="item.name"
      />
      <input
        type="text"
        placeholder="Description"
        class="input input-ghost w-full max-w-xs p-0 text-center"
        :value="item.description"
      />
      <div class="divider m-0"></div>
      <p class="card-title block">
        $
        <input
          type="text"
          placeholder="Price"
          class="input input-bordered w-16 p-0 text-center"
          :value="item.price.toFixed(DEFAULT_PRICE_DECIMAL_PLACES)"
        />
      </p>
      <div class="card-actions justify-between mt-4">
        <input
          type="text"
          placeholder="Qty"
          class="input input-bordered w-12 p-0 text-center"
          :value="item.quantity"
        />
        <div class="admin-mod-selection">
          <button
            :disabled="isLoading"
            @click="
              async (event) => {
                await deleteItem(item.id);
                await updateCurrentItems();
              }
            "
            class="btn btn-primary mx-2"
          >
            Delete
          </button>
          <button class="btn btn-primary mx-2">Save</button>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
