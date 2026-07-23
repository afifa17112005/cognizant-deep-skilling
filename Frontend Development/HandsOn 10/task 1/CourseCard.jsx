import { useDispatch } from "react-redux";

import { enroll } from "../redux/enrollmentSlice";

function CourseCard({

id,
name,
code,
credits,
grade

}){

const dispatch = useDispatch();

const handleEnroll = () => {

dispatch(

enroll({

id,
name,
code,
credits,
grade

})

);

};

return(

<div className="card">

<h3>{name}</h3>

<p>{code}</p>

<p>Credits : {credits}</p>

<p>Grade : {grade}</p>

<button onClick={handleEnroll}>

Enroll

</button>

</div>

);

}

export default CourseCard;