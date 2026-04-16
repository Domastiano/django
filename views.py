def show_exam_result(request, course_id, submission_id):
    course = Course.objects.get(pk=course_id)
    submission = Submission.objects.get(pk=submission_id)

    choices = submission.choices.all()

    total_grade = 0
    earned_grade = 0
    question_results = []

    for question in course.question_set.all():
        total_grade += question.grade

        selected_choices = [choice for choice in choices if choice.question == question]
        selected_ids = [choice.id for choice in selected_choices]

        is_correct = question.is_get_score(selected_ids)

        if is_correct:
            earned_grade += question.grade

        question_results.append({
            'question': question,
            'is_correct': is_correct,
            'selected_choices': selected_choices,
        })

    percentage = (earned_grade / total_grade) * 100 if total_grade > 0 else 0
    passed = percentage >= 70

    context = {
        'course': course,
        'total_grade': total_grade,
        'earned_grade': earned_grade,
        'percentage': percentage,
        'passed': passed,
        'question_results': question_results
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
