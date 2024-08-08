import React, { useEffect, useState } from 'react';
import {getSolutions } from './apiService';

/**
 * @summary gets the solutions for the issue and renders them
 * @returns 
 */
const Solutions = () => {
  const [soln, setSolutions] = useState(null);

  useEffect(() => {
    const fetchSolutions = async () => {
      try {
        const solutions = await getSolutions(1); // Fetch user with ID 1
        setSolutions(solutions[0]);
        console.log(soln)
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    fetchSolutions();
  }, []);

  return (
    <div>
      {soln && (
          <p class="card-text text-left margin-text"><b>Recommended Solutions:</b> {soln.solutions}</p>
      )}
    </div>
  );
};

export default Solutions;