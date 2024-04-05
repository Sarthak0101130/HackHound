// // Function to send CSV file to the API
// const baseUrl12 = 'http://localhost:2200';
// async function sendCSVFileToAPI(board, total_marks) {
//     try {
//       const formData = new FormData();
      
//       // Append the CSV file to the FormData object
//       formData.append('Board', board);
//         formData.append('total_marks', total_marks);
  
//       const response = await fetch(`${baseUrl12}/result`, {
//         method: 'POST',
//         body: formData
//       });
  
//       if (!response.ok) {
//         throw new Error(`API request failed with status ${response.status}`);
//       }
  
//       const responseData = await response.json();
//       console.log(responseData); // This will log the response from your Python API
//     } catch (error) {
//       console.error('Error sending variables to API:', error);
//     }
//   }
  
// var board=document.getElementById("board").value
// var total_marks= document.getElementById("total_marks").value
  