import React, { useEffect, useState } from 'react';
import { Line, Doughnut, PolarArea, Pie, Radar, Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  BarElement,
  LineElement,
  PointElement,
  RadialLinearScale,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Register charts and necessary components
ChartJS.register(
  ArcElement,
  BarElement,
  LineElement,
  PointElement,
  RadialLinearScale,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend
);

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    (async () => {
      const res = await fetch('http://localhost:5000/reports/random');
      const json = await res.json();
      const data = json.data;
      console.log(data);

      // Define eye-pleasing colors
      const eyePleasingColors = [
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
      ];

      // Transform the data into the format expected by Chart.js
      const transformedData = {
        intensity: {
          labels: [...new Set(data?.map((item) => item.intensity))].sort(
            (a, b) => a - b
          ),
          datasets: [
            {
              label: "Intensity",
              data: data?.map((item) => item.intensity).sort((a, b) => a - b),
              backgroundColor: eyePleasingColors,
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        },
        likelihood: {
          labels:  [...new Set(data?.map((item) => item.likelihood))],
          datasets: [
            {
              label: 'Likelihood',
              data: [...new Set(data?.map((item) => item.likelihood))].map((likelihood) =>
                data?.filter((item) => item.likelihood === likelihood).length
              ),
              backgroundColor: eyePleasingColors,
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
            },
          ],
        },
        relevance: {
          labels:  [...new Set(data?.map((item) => item.relevance))],
          datasets: [
            {
              label: 'Relevance',
              data: [...new Set(data?.map((item) => item.relevance))].map((relevance) =>
                data?.filter((item) => item.relevance === relevance).length
              ),
        backgroundColor: [
  'rgba(255, 215, 0, 0.5)',   // Yellow
  'rgba(255, 165, 0, 0.5)',   // Orange
  'rgba(255, 0, 0, 0.5)',     // Red
  'rgba(0, 255, 0, 0.5)',     // Green
  'rgba(0, 0, 255, 0.5)',     // Blue
  'rgba(128, 0, 128, 0.5)',   // Purple
  'rgba(255, 192, 203, 0.5)', // Pink
  'rgba(255, 255, 0, 0.5)'    // Lime
],
borderColor: 'rgba(255, 206, 86, 1)',
borderWidth: 1,
            },
          ],
        },
        country: {
          labels: [...new Set(data?.map((item) => item.country))],
          datasets: [
            {
              label: 'Country',
              data: [...new Set(data?.map((item) => item.country))].map((country) =>
                data?.filter((item) => item.country === country).length
              ),
              backgroundColor: eyePleasingColors,
              borderColor: 'rgba(255, 255, 255, 1)',
              borderWidth: 1,
            },
          ],
        },
        topic: {
          labels: [...new Set(data?.map((item) => item.topic))],
          datasets: [
            {
              label: 'Topic',
              data: [...new Set(data?.map((item) => item.topic))].map((topic) =>
                data?.filter((item) => item.topic === topic).length
              ),
              backgroundColor: eyePleasingColors,
              borderColor: 'rgba(255, 255, 255, 1)',
              borderWidth: 1,
            },
          ],
        },
        region: {
          labels: [...new Set(data?.map((item) => item.region))],
          datasets: [
            {
              label: 'Region',
              data: [...new Set(data?.map((item) => item.region))].map((region) =>
                data?.filter((item) => item.region === region).length
              ),
              backgroundColor: eyePleasingColors,
              borderColor: 'rgba(255, 255, 255, 1)',
              borderWidth: 1,
            },
          ],
        },
      };
      console.log(transformedData);
      setData(transformedData);
    })();
  }, []);

  return (
    <div>
      {data && (
        <div
        style={{
          display:"flex",
          flexWrap:"wrap",
          gap:"50px",
          width:"calc(100vw -200px)"
        }}
        > <div
            style={{
              maxWidth:"500px",
              maxHeight: '1000px',
            }}>
              <h2 style={{
                marginLeft:'20px',
            
              }}>Intensity</h2>

          <Line data={data.intensity} />
        </div>
        <div
        style={{
          maxWidth:'500px',
          maxHeight: '400px',
        }}>
          <h2>Likelihood</h2>
          <Doughnut data={data.likelihood} />
        </div>
         <div
         style={{
          maxWidth:'600px',
          maxHeight: '727px',
         }}>
          <h2>Relevance</h2>

          <PolarArea data={data.relevance} />
         </div>
         <div
         style={{
          maxWidth:'500px',
          maxHeight: '727px',
          width: '462px'
         }}>
            < h3 style={{
              marginLeft:'20px',
              width:'100%'
            }}>
            Country
            </h3>
            <Pie data={data.country} />
         </div>
         <div 
         style={{
          maxWidth:'700px',
          maxHeight: '727px',
          width: '462px'
         }}>
          <h2>Topic</h2>

            <Doughnut data={data.topic} />
         </div>
         <div
         style={{
          maxWidth:'700px',
          maxHeight: '727px',
          width: '462px'

         }}>  
         <h2>Region</h2>

            <Pie data={data.region} />
         </div>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
