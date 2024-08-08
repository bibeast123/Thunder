import React, { useEffect, useState } from 'react';
import { getSummary} from './apiService';

/**
 * @summary gets the summary text of the user and renders it
 * @returns 
 */
const Summary = () => {
  
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const summaryText = await getSummary(1); // Fetch user with ID 1
        setSummary(summaryText[0]);
        console.log(summaryText)
      } catch (error) {
        console.error('Error fetching summary:', error);
      }
    };

    fetchSummary();
  }, []);

  return (
    <div>
      {summary && (
        <p class="card-text text-left margin-text"><b>Summary:</b> {summary.summary}</p>
      )}
    </div>
  );
};

export default Summary;