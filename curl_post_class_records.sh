#!/bin/bash
curl -X POST http://127.0.0.1:7776/class_record -H 'Content-Type: application/json' -d '{"student_id":"2","assignment_id":"10","marks":"100"}'