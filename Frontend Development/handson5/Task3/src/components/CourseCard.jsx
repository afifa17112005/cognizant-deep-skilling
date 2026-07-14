function CourseCard({ title, id }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <p>Course ID: {id}</p>
    </div>
  );
}

export default CourseCard;