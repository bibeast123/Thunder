import React from 'react';
import DefaultSidebar from './DefaultSidebar';
import Dashboard from './Dashboard';

/**
 * @summary renders dashboard layout
 * @returns 
 */
function DashboardLayout() {
  return (
    <div class="mt-24">
      <DefaultSidebar />
      <Dashboard />
    </div>
  );
}

export default DashboardLayout;