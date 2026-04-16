def submit(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)
    enrollment = Enrollment.objects.get(user=user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    
    for choice_id in request.POST.getlist('choice'):
        choice = Choice.objects.get(id=choice_id)
        submission.choices.add(choice)
    
    return redirect('show_exam_result', course_id=course_id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.get(id=submission_id)
    selected_choices = submission.choices.all()
    
    total_grade = 0
    earned_grade = 0
    
    for question in course.question_set.all():
        total_grade += question.grade
        selected_ids = [c.id for c in selected_choices if c.question == question]
        if question.is_get_score(selected_ids):
            earned_grade += question.grade
    
    passed = earned_grade >= total_grade * 0.7
    
    context = {
        'course': course,
        'submission': submission,
        'selected_choices': selected_choices,
        'total_grade': total_grade,
        'earned_grade': earned_grade,
        'passed': passed,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
