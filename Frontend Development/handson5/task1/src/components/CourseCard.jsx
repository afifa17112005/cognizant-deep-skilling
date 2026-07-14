function CourseCard(props) {
  return (
    <div className="course-card">
      <h2>{props.name}</h2>

      <p><strong>Code:</strong> {props.code}</p>

      <p><strong>Credits:</strong> {props.credits}</p>

      <p><strong>Grade:</strong> {props.grade}</p>
    </div>
  );
}

export default CourseCard;