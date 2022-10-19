#!/bin/bash
curl -X POST http://127.0.0.1:7776/api/class_record -H 'Content-Type: application/json' -d '{"student_id":"3","assignment_id":"10","marks":"100"}'