import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api/v1/research-publications/";

export const getPublications = async () => {
  try {
    const response = await axios.get(API_BASE_URL);
    return response;
  } catch (error) {
    console.error("Error al obtener los elementos:", error);
    throw error;
  }
};
