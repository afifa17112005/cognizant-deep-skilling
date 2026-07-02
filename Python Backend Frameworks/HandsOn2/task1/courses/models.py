class Meta:
    unique_together = [['student', 'course']]

def __str__(self):
    return f"{self.student} - {self.course}"