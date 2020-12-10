# -*- coding: UTF-8 -*-

class ResourceNotFoundException(Exception):
    def __init__(self, scope, identify):
        self.scope = scope
        self.identify = identify
        message = "找不到%s: %s" % (scope, identify)
        super().__init__(message)


class StudentNotFoundException(ResourceNotFoundException):
    def __init__(self, job_id):
        self.node_id = job_id
        super().__init__("学生", str(job_id))
