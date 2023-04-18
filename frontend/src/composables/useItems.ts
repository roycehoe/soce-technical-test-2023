import { Err, Ok, Result } from "ts-results";
import { ref } from "vue";
import { client } from "../services";
import { ShopItemIn, ShopItemOut } from "./useItem";

export const currentItems = ref([] as ShopItemIn[]);

export function useItems() {
  async function getItems(): Promise<Result<ShopItemOut[], string>> {
    try {
      const response = await client.get("/items/");
      return Ok(response.data as ShopItemIn[]);
    } catch (error) {
      console.log(error);
      return Err("error occured retrieving all items");
    }
  }

  async function updateCurrentItems(): Promise<void> {
    const { ok: isSuccessful, val: response } = await getItems();
    if (isSuccessful) {
      currentItems.value = response as ShopItemIn[];
      return;
    }
    console.log(response);
  }

  return { getItems, updateCurrentItems };
}
