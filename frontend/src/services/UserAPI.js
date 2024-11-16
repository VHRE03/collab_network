import axios from "axios";

const UsersAPI = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/users/",
});

export const getUser = (id) => UsersAPI.get(`/${id}`);
