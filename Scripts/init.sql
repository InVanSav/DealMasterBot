CREATE TABLE IF NOT EXISTS "Users" (
  "user_id" uuid PRIMARY KEY,
  "first_name" VARCHAR(255) NOT NULL,
  "last_name" VARCHAR(255) NOT NULL,
  "phone_number" VARCHAR(255) NOT NULL,
  "from_bot" BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS "Answers" (
  "answer_id" uuid PRIMARY KEY,
  "user_id" uuid NOT NULL REFERENCES "Users"("user_id"),
  "first_question" TEXT NOT NULL,
  "second_question" TEXT NOT NULL,
  "third_question" TEXT NOT NULL,
  "fourth_question" TEXT NOT NULL
);
