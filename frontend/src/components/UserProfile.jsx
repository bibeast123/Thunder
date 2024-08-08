import React, { useEffect, useState } from 'react';
import { getUser } from './apiService';
import Card from 'react-bootstrap/Card'; // Assuming you are using react-bootstrap

/**
 * @summary gets information about the user and renders this information
 * @returns 
 */
const UserProfile = () => {
  
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userData = await getUser(1); // Fetch user with ID 1
        setUser(userData);
        console.log(userData)
      } catch (error) {
        console.error('Error fetching user:', error);
      }
    };

    fetchUser();
  }, []);

  return (
    <div class="grid grid-cols-2 gap-6 mb-4">
      {/* Profile information */}
      {user && (
        <Card className="text-left card-hover">
          <Card.Body>
            <Card.Title>Profile Information</Card.Title>
            <p class="card-text text-left margin-text"><b>Name:</b> {user.firstname} {user.lastname}</p>
            <p class="card-text text-left margin-text"><b>Current Internet Plan:</b> {user.preferences.CurrentInternetPlan}</p>
            <p class="card-text text-left margin-text"><b>Preferred Langauge:</b> {user.preferences.Language}</p>
            <p class="card-text text-left margin-text"><b>Oustanding Balance:</b> {user.preferences.OutstandingBalance}</p>
            <p class="card-text text-left margin-text"><b>Prefered Call Time</b>: {user.preferences.PreferredCallTime}</p>
            <p class="card-text text-left margin-text"><b>Time as a customer:</b> {user.preferences.TimeAsCustomer} months</p>
          </Card.Body>
        </Card>
      )}
      {/* Profile history */}
      {user && (
        <Card className="text-left card-hover">
          <Card.Body>
            <Card.Title>Profile History</Card.Title>
            {/** <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>*/}
            <p class="card-text text-left margin-text"><b>Past Problems and Solutions:</b> {user.preferences.PastProblemsAndSolutions}</p>
            <p class="card-text text-left margin-text"><b>Recurring Issues:</b> {user.preferences.RecurringIssues}</p>
            <p class="card-text text-left margin-text"><b>Satisfaction Score:</b> {user.preferences.SatisfactionScore}</p>
            <p class="card-text text-left margin-text"><b>Subscriptions:</b> {user.preferences.Subscriptions}</p>
            <p class="card-text text-left margin-text"><b>Time of Call:</b> {user.updated_at}</p>
          </Card.Body>
        </Card>
      )}
    </div>
  );
};
export default UserProfile;