def show_exam_result(request, course_id, submission_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.get(id=submission_id)
    selected_choices = submission.choices.all()
    
    total_grade = 0
    earned_grade = 0
    question_results = []
    
    for question in course.question_set.all():
        total_grade += question.grade
        selected_ids = [c.id for c in selected_choices if c.question == question]
        if question.is_get_score(selected_ids):
            earned_grade += question.grade
            correct = True
        else:
            correct = False
        
        selected_texts = [c.content for c in selected_choices if c.question == question]
        correct_texts = [c.content for c in question.choice_set.filter(is_correct=True)]
        
        question_results.append({
            'question': question,
            'correct': correct,
            'selected_choices': selected_texts,
            'correct_choices': correct_texts,
        })
    
    percentage = (earned_grade / total_grade) * 100 if total_grade > 0 else 0
    passed = earned_grade >= total_grade * 0.7  # próg zaliczenia (70%)
    
    context = {
        'course': course,
        'submission': submission,
        'total_grade': total_grade,
        'earned_grade': earned_grade,
        'percentage': percentage,
        'passed': passed,
        'question_results': question_results,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
