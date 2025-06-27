#!/bin/bash
echo "Running backend tests..."
cd ../src/tests
pytest
echo "Running frontend tests..."
cd ../../frontend/src/tests
npm run test
echo "All tests complete!"
