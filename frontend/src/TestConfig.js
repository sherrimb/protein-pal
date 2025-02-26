import React from 'react';
import config from './config';

function TestConfig() {
  return (
    <div style={{ padding: '20px' }}>
      <h2>Config Test</h2>
      <pre style={{ backgroundColor: '#f0f0f0', padding: '10px' }}>
        Region: {config.REGION}<br/>
        User Pool ID: {config.USER_POOL_ID}<br/>
        Client ID: {config.USER_POOL_WEB_CLIENT_ID}<br/>
        API URL: {config.API_URL}
      </pre>
    </div>
  );
}

export default TestConfig;