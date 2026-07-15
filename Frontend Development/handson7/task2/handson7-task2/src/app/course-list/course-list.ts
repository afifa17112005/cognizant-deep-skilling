import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CourseService } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseList {

  private courseService = inject(CourseService);

  courses: any[] = [];

  loading = true;

  ngOnInit() {

    this.courseService.getCourses().subscribe({

      next: (data) => {

        this.courses = data;

        this.loading = false;

      },

      error: (err) => {

        console.log(err);

        this.loading = false;

      }

    });

  }

}