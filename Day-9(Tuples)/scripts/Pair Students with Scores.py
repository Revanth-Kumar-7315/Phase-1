# Pair Students with Scores with Tuples
def pair_students_with_scores(students, scores):
    """
    This function pairs students with their corresponding scores using tuples.

    :param students: A list of student names.
    :param scores: A list of scores corresponding to the students.
    :return: A list of tuples where each tuple contains a student and their score.
    """
    if len(students) != len(scores):
        raise ValueError("The number of students must match the number of scores.")

    paired_list = []
    for student, score in zip(students, scores):
        paired_list.append((student, score))

    return paired_list
