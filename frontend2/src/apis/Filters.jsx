import React, { useEffect, useState } from 'react';

function Filters() {
  const [data, setData] = useState(null);
  const [apiEndpoint, setApiEndpoint] = useState('https://api.example.com/');

  useEffect(() => {
    fetch(apiEndpoint)
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error:', error));
  }, [apiEndpoint]);

  const updateApiEndpoint = (newEndpoint) => {
    setApiEndpoint(newEndpoint);
  }

  return (
    <div>
      {/* Render your data here. This is just a placeholder. */}
      {data && <div>{JSON.stringify(data)}</div>}
      {/* Add a button or other UI element to update the API endpoint */}
      <button onClick={() => updateApiEndpoint('https://new-api.example.com/')}>Update API Endpoint</button>
    </div>
  );
}

export default Filters;