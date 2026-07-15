import { Component, input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  imports: [],
  templateUrl: './course-card.html',
  styleUrl: './course-card.css'
})
export class CourseCard {

  name = input<string>();

  code = input<string>();

  credits = input<number>();

  grade = input<string>();

}