import React, { useEffect, useState } from 'react';
import {getCategory } from './apiService';

/**
 * @summary gets categories of user call and renders cared of this data
 * @returns 
 */
const Categories = () => {

  const [categ, setCategory] = useState(null);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const categories = await getCategory(1);
        setCategory(categories[0]);
        console.log(categories)
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    fetchCategories();
  }, []);

  return (
    <div>
      {categ && (
        <div>
          <p class="card-text text-left margin-text"><b>Current Issue:</b> {categ.issue}</p>
          <p class="card-text text-left margin-text"><b>Urgency</b> {categ.urgency}</p>
        </div>
      )}
    </div>
  );
};

export default Categories;