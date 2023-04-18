import { Err, Result } from "ts-results";
import { client } from "../services";
import { ShopItemIn } from "./useItem";

export function useItems() {
  async function getItems(): Promise<Result<ShopItemIn[], string>> {
    try {
      const response = await client.post("/items/");
      return response.data;
    } catch (error) {
      console.log(error);
      return Err("error occured retrieving all items");
    }
  }

  return { getItems };
}
