1.select  courses.name, teachers.name
  from courses
  inner join teachers on courses.teacher_id=teachers.teachers_id;

2. select  teachers.name
  from courses
  inner join teachers on courses.teacher_id=teachers.teachers_id
  group by teachers.teachers_id
  having count (teachers.teachers_id)>1;

3.select teachers.name
  from  teachers
  left join courses on courses.teacher_id=teachers.teachers_id
  where courses.courseid is null
