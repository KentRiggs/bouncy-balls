import React, { useState } from 'react';
import './App.css';

function App() {
  const [numBalls, setNumBalls] = useState(20);
  const [ballSize, setBallSize] = useState(10); // Default ball size
  const [ballColor, setBallColor] = useState('RED'); // Default ball color
  const [ballSpeed, setBallSpeed] = useState(2); // Default ball speed

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://127.0.0.1:5000/run_pygame', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        numBalls,
        ballSize,
        ballColor,
        ballSpeed,
      }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="numBalls">Number of Balls:</label>
        <input
          type="number"
          id="numBalls"
          value={numBalls}
          onChange={(e) => setNumBalls(parseInt(e.target.value, 10))}
        />
      </div>
      <div>
        <label htmlFor="ballSize">Ball Size:</label>
        <input
          type="number"
          id="ballSize"
          value={ballSize}
          onChange={(e) => setBallSize(parseInt(e.target.value, 10))}
        />
      </div>
      <div>
        <label htmlFor="ballColor">Ball Color:</label>
        <select
          id="ballColor"
          value={ballColor}
          onChange={(e) => setBallColor(e.target.value)}
        >
          {/* Option values based on available colors */}
          <option value="RED">Red</option>
          <option value="GREEN">Green</option>
          <option value="BLUE">Blue</option>
          <option value="YELLOW">Yellow</option>
          <option value="PURPLE">Purple</option>
          <option value="ORANGE">Orange</option>
          <option value="CYAN">Cyan</option>
          <option value="MAGENTA">Magenta</option>
        </select>
      </div>
      <div>
        <label htmlFor="ballSpeed">Ball Speed:</label>
        <input
          type="number"
          id="ballSpeed"
          value={ballSpeed}
          onChange={(e) => setBallSpeed(parseFloat(e.target.value))}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

export default App;