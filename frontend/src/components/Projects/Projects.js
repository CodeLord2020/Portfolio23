// import { Container, Row, Spinner, Col } from "react-bootstrap";
// import ProjectCard from "./ProjectCards";
// import Particle from "../Particle";
// import React, { useState, useEffect } from "react";

// function Projects() {
//   useEffect(() => {
//     getProjectsData()
//   }, [])

//   const [projectsData, setProjectsData] = useState([]);
//   const [loading, setLoading] = useState(true); // Track the loading state

//   let getProjectsData = async () => {
//     try {
//       let response = await fetch('https://muzamil-ali.onrender.com/projects', {
//         method: 'GET',
//         headers: {
//           'Content-Type': 'application/json',
//         }
//       })
//       let data = await response.json()
//       setProjectsData(data)
//       setLoading(false); // Set loading state to false after successful API response
//     } catch (error) {
//       console.error("Error fetching projects data:", error);
//       setLoading(false); // Set loading state to false in case of error
//     }
//   }

//   return (
//     <Container fluid className="project-section">
//       <Particle />
//       <Container>
//         <h1 className="project-heading">
//           My Recent <strong className="purple">Works </strong>
//         </h1>
//         <p style={{ color: "white" }}>
//           Here are a few projects I've worked on.
//         </p>

//         {loading ? ( // Render the loading animation if still loading
//           <Spinner animation="border" variant="primary" role="status">
//             <span className="sr-only"></span>
//           </Spinner>
//         ) : (
//           <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>
//             {projectsData.map((project, idx) => (
//               <Col md={4} className="project-card" key={idx}>
//                 <ProjectCard
//                   imgPath={project.image}
//                   title={project.title}
//                   description={project.description}
//                   ghLink={project.src_url}
//                   demoLink={project.project_url}
//                 />
//               </Col>
//             ))}
//           </Row>
//         )}
//       </Container>
//     </Container>
//   );
// }

// export default Projects;
