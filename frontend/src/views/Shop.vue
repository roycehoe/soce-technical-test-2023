<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import { ShopItemIn } from "../composables/useItem";
import { useItems } from "../composables/useItems";
import { DEFAULT_PRICE_DECIMAL_PLACES } from "../constants";

const { getItems } = useItems();

const shopItems = ref([] as ShopItemIn[]);

async function fetchShopItemData() {
  const { ok: isSuccessful, val: response } = await getItems();
  if (isSuccessful) {
    shopItems.value = response as ShopItemIn[];
    return;
  }
  console.log(response);
}

onBeforeMount(fetchShopItemData);
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex flex-wrap mx-24 text-center">
      <div v-for="item in shopItems" class="w-96 m-6">
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <p class="card-title text-center block">{{ item.name }}</p>
            <p>{{ item.description }}</p>
            <div class="divider m-0"></div>
            <p class="my-2 card-title block">
              ${{ item.price.toFixed(DEFAULT_PRICE_DECIMAL_PLACES) }}
            </p>
            <div class="card-actions justify-between mt-2">
              <select class="select select-primary">
                <option selected>0</option>
                <option v-for="quantity in item.quantity">
                  {{ quantity }}
                </option>
              </select>
              <button class="btn btn-primary">Add to cart</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
