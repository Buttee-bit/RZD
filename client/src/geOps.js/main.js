
import axios from 'axios';

const BASE_URL = 'https://api.geops.io/';

// Функция для выполнения запроса к Geocoding API
export async function geocode(address) {
  try {
    const response = await axios.get(`${BASE_URL}/geocode`, {
      params: {
        text: address,
      },
    });

    return response.data;
  } catch (error) {
    console.error('Ошибка при выполнении запроса к Geocoding API:', error);
    throw error;
  }
}