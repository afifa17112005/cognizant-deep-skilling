import apiClient from "./apiClient";

export const getAllCourses = async () => {
  const posts = await apiClient.get("/posts");

  return posts.slice(0, 5).map((post) => ({
    id: post.id,
    name: post.title,
    code: `CS10${post.id}`,
    credits: 4,
    grade: "A",
  }));
};

export const getCourseById = async (id) => {
  const post = await apiClient.get(`/posts/${id}`);

  return {
    id: post.id,
    name: post.title,
    code: `CS10${post.id}`,
    credits: 4,
    grade: "A",
  };
};