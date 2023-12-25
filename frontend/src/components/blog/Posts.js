import { Container, Row, Col, Spinner } from "react-bootstrap";
import PostsCard from "./PostsCards";
import Particle from "../Particle";
import React, { useState, useEffect } from "react";

function Posts() {
  const [blogPosts, setBlogPosts] = useState([]);
  const [loading, setLoading] = useState(true); // Track the loading state

  useEffect(() => {
    getPostsData();
  }, []);

  let getPostsData = async () => {
    try {
      let response = await fetch("https://muzamil-ali.onrender.com/posts", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      setBlogPosts(data);
      setLoading(false); // Set loading state to false after successful API response
    } catch (error) {
      console.error("Error fetching blog posts:", error);
      setLoading(false); // Set loading state to false in case of error
    }
  };

  return (
    <Container fluid className="project-section">
      <Particle />
      <Container>
        <h1 className="project-heading">
          My Recent <strong className="purple">Posts </strong>
        </h1>
        <p style={{ color: "white" }}>
          Here are a few posts I've published recently.
        </p>

        {loading ? ( // Render the loading animation if still loading
          <Spinner animation="border" variant="primary" role="status">
            <span className="sr-only"></span>
          </Spinner>
        ) : (
          <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>
            {blogPosts.map((post) => (
              <Col md={4} className="project-card" key={post.id}>
                <PostsCard
                  imgPath={post.image}
                  title={post.title}
                  poLink={"https://muzamil-blog.netlify.app/blog/" + post.slug}
                />
              </Col>
            ))}
          </Row>
        )}
      </Container>
    </Container>
  );
}

export default Posts;
