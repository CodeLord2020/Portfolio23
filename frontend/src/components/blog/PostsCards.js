import React from "react";
import Card from "react-bootstrap/Card";

function PostsCards(props) {
  return (
    <Card className="project-card-view">
      <Card.Img variant="top" src={props.imgPath} alt="card-img" />
      <Card.Body>
        <a
          href={props.poLink}
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: "white" }}
        >
          {props.title}
        </a>
      </Card.Body>
    </Card>
  );
}
export default PostsCards;
