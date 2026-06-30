from sqlalchemy import text


def test_add_student(db_engine):
    test_user_id = 888881
    with db_engine.connect() as connection:
        try:
            connection.execute(text(
                f"DELETE FROM student"
                f"WHERE user_id = {test_user_id}"
                ))

            connection.execute(
                text("""
                    INSERT INTO student (
                     user_id,
                     level,
                     education_form,
                     subject_id
                    )
                    VALUES (:user_id, :level, :education_form, :subject_id)
                """),
                {
                    "user_id": test_user_id,
                    "level": "bachelor",
                    "education_form": "full-time",
                    "subject_id": 101
                }
            )

            result = connection.execute(
                text(
                    "SELECT level,"
                    "education_form FROM student WHERE user_id = :user_id"
                    ),
                {"user_id": test_user_id}
            ).fetchone()

            assert result is not None
            assert result[0] == "bachelor"
            assert result[1] == "full-time"
        finally:
            connection.execute(text(
                f"DELETE FROM student"
                f"WHERE user_id = {test_user_id}"
                ))


def test_update_student(db_engine):
    test_user_id = 888882
    with db_engine.connect() as connection:
        try:
            connection.execute(text(
                f"DELETE FROM student"
                f"WHERE user_id = {test_user_id}"
                ))

            connection.execute(
                text("""
                    INSERT INTO student (
                     user_id, level,
                     education_form,
                     subject_id
                     )
                    VALUES (:user_id, :level, :education_form, :subject_id)
                """),
                {
                    "user_id": test_user_id,
                    "level": "bachelor",
                    "education_form": "full-time",
                    "subject_id": 101
                }
            )

            connection.execute(
                text("""
                     UPDATE student
                     SET level = :new_level
                     WHERE user_id = :user_id
                     """),
                {"user_id": test_user_id, "new_level": "master"}
            )

            result = connection.execute(
                text("SELECT level FROM student WHERE user_id = :user_id"),
                {"user_id": test_user_id}
            ).fetchone()

            assert result[0] == "master"
        finally:
            connection.execute(text(
                f"DELETE FROM student"
                f"WHERE user_id = {test_user_id}"
                ))


def test_delete_student(db_engine):
    test_user_id = 888883
    with db_engine.connect() as connection:
        try:
            connection.execute(text(
                f"DELETE FROM student"
                f"WHERE user_id = {test_user_id}"
                ))

            connection.execute(
                text("""
                    INSERT INTO student (
                     user_id,
                     level,
                     education_form,
                     subject_id
                     )
                    VALUES (:user_id, :level, :education_form, :subject_id)
                """),
                {
                    "user_id": test_user_id,
                    "level": "bachelor",
                    "education_form": "full-time",
                    "subject_id": 101
                    }
            )

            connection.execute(text(
                "DELETE FROM student WHERE user_id = :user_id"),
                {"user_id": test_user_id}
                )

            result = connection.execute(
                text("SELECT * FROM student WHERE user_id = :user_id"),
                {"user_id": test_user_id}
            ).fetchone()

            assert result is None
        finally:
            connection.execute(text(
                f"DELETE FROM student"
                f"WHERE user_id = {test_user_id}"))
