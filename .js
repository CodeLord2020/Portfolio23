import { Container, Row, Col } from "react-bootstrap";
import PostsCard from "./PostsCards";
import Particle from "../Particle";
import React, { useState, useEffect } from "react";

function Posts() {
  const [blogPosts, setBlogPosts] = useState([]);
  useEffect(() => {
    getPostsData()
  }, [])

  let getPostsData = async () => {
    let response = await fetch('https://muzamil-ali.onrender.com/posts', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    })
    let data = await response.json()
    setBlogPosts(data)
  }

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

        <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>

          {blogPosts.map((post) => (
            <Col md={4} className="project-card" key={post.id}>
              <PostsCard
                imgPath={post.image}
                title={post.title}
                poLink={'https://muzamil-blog.netlify.app/blog/' + post.slug}
              />
            </Col>
          ))}

        </Row>
      </Container>
    </Container>
  );
}