import { useEffect } from "react";

import { useDispatch,useSelector } from "react-redux";

import {

fetchAllCourses,

selectCourses,

selectCoursesLoading,

selectCoursesError

}

from "../features/courses/courseSlice";

function CoursesPage(){

const dispatch=useDispatch();

const courses=useSelector(selectCourses);

const loading=useSelector(selectCoursesLoading);

const error=useSelector(selectCoursesError);

useEffect(()=>{

dispatch(fetchAllCourses());

},[dispatch]);

if(loading){

return <h2>Loading...</h2>;

}

if(error){

return <h2>{error}</h2>;

}

return(

<div>

<h2>Courses</h2>

{

courses.map(course=>(

<div

key={course.id}

style={{

border:"1px solid gray",

padding:"15px",

marginBottom:"10px"

}}

>

<h3>{course.name}</h3>

<p>{course.code}</p>

<p>{course.credits} Credits</p>

<p>Grade : {course.grade}</p>

</div>

))

}

</div>

);

}

export default CoursesPage;