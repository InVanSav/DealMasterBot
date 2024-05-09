CREATE TABLE IF NOT EXISTS "Users" (
  "user_id" uuid PRIMARY KEY,
  "telegram_name" VARCHAR(255) NOT NULL,
  "phone_number" VARCHAR(255) NOT NULL,
  "from_bot" BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS "Answers" (
  "answer_id" uuid PRIMARY KEY,
  "user_id" uuid NOT NULL REFERENCES "Users"("user_id"),
  "city" VARCHAR(255) NOT NULL,
  "district" VARCHAR(255) NOT NULL,
  "area" VARCHAR(255) NOT NULL,
  "price" VARCHAR(255) NOT NULL
);
