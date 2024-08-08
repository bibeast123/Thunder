import React from 'react';
import { Card} from 'react-bootstrap';
import UserProfile from './UserProfile';
import Summary from './Summary';
import Categories from './Categories';
import Solutions from './Solutions';

/**
 * @summary Dashboard of user. Should contain cards that containe
 * information from api calls
 */
const Dashboard = () => {

  return (
    <div class="ml-48 -mr-32">
      <div class="ml-32 -mr-64">
        <div class="p-4  rounded-lg dark:border-gray-700">
            
          {/* Profile card*/}
          <UserProfile/>

          <div class="grid grid-cols-1 gap-6 mb-4 ">
            {/* Summary Card */}
            <Card className="card text-left card-hover">
              <Card.Body>
                <Card.Title>Summary</Card.Title>
                <Card.Text>
                  <Summary/>
                </Card.Text>
              </Card.Body>
            </Card>
          </div>

          <div class="grid grid-cols-2 gap-6 mb-4">
            {/* Current Issue Card */}
            <Card className="card text-left card-hover">
              <Card.Body>
                <Card.Title>Current Issue</Card.Title>
                <Card.Text>
                  <Categories/>
                </Card.Text>
              </Card.Body>
            </Card>

            {/* Prvious calls card */}
            <Card className="card text-left card-hover">
              <Card.Body>
                <Card.Title>Previous Calls</Card.Title>
                <Card.Text>
                  <p class="card-text text-left margin-text"><b>Time of Call:</b> Wed, 17 Jul 2024 16:54:11 GMT</p>
                  <p class="card-text text-left margin-text"><b>Reason: </b>  User had a billing issue. </p>
                </Card.Text>
              </Card.Body>
            </Card>
          </div>

          <div class="grid grid-cols-1 gap-6 mb-4">
            {/* Recommend SOlutions Card */}
            <Card className="card text-left card-hover">
              <Card.Body>
                <Card.Title>Recommended Solutions</Card.Title>
                <Card.Text>
                  <Solutions/>
                  <p class="card-text text-left margin-text">
                    <b>Context: </b>  
                    The current issue is not related to any issues the customer had in the past.
                  </p>
                </Card.Text>
              </Card.Body>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;