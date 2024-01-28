# Backend

See the root README for more details.

Use ```pigar generate``` to update the requirements.txt after installing a new package.
Auto-format the code using Black.
Make sure the tests pass by running pytest.

### Modifying the database schema
1. Modify the SQLAlchemy models as needed
2. In the backend Docker container, run ```alembic revision --autogenerate -m "SHORT CHANGES DESCRIPTION"```
3. Revise the newly created migration file
4. Run ```alembic upgrade head``` and test if the changes works
5. Run tests to ensure everything still works - fix bugs or rollback the change if necessary
