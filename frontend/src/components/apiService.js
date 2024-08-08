import axios from 'axios';

// Flask pai url
const API_BASE_URL = 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

/**
 * 
 * @param {int} userId 
 * @returns user information
 */
export const getUser = async (userId) => {
  try {
    const response = await api.get(`/users/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
};

/**
 * 
 * @param {int} userId 
 * @returns summary text of call
 */
export const getSummary = async (userId) => {
  try {
    const response = await api.get(`/ml/summary/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching summary:', error);
    throw error;
  }
};

/**
 * 
 * @param {int} userId 
 * @returns category and urgency of call 
 */
export const getCategory = async (userId) => {
  try {
    const response = await api.get(`/ml/categorize/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching categories:', error);
    throw error;
  }
};

/**
 * 
 * @param {int} userId 
 * @returns solution of issue
 */
export const getSolutions = async (userId) => {
  try {
    const response = await api.get(`/ml/solutions/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching solutions:', error);
    throw error;
  }
};