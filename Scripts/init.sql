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

CREATE TABLE IF NOT EXISTS "Cities" (
  "city_id" uuid PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "Districts" (
  "district_id" uuid PRIMARY KEY,
  "city_id" uuid NOT NULL REFERENCES "Cities"("city_id"),
  "name" VARCHAR(255) NOT NULL
);

INSERT INTO "Cities" ("city_id", "name") VALUES
('e1389007-141c-4f43-9a03-1ddb8c153b32', 'Волгоград'),
('bdbc5317-ea1f-492c-ade4-d0f5c018e00e', 'Санкт-Петербург');

INSERT INTO "Districts" ("district_id", "city_id", "name") VALUES
('fbc11ef5-ad27-4f5e-851c-08df9ae3e21d', 'e1389007-141c-4f43-9a03-1ddb8c153b32', 'Ворошиловский'),
('80704909-20c6-4e86-994b-24d9e8b93797', 'e1389007-141c-4f43-9a03-1ddb8c153b32', 'Советский'),
('8c0980b3-cd41-4ace-b5e1-9248d959b6b4', 'e1389007-141c-4f43-9a03-1ddb8c153b32', 'Тракторозаводский'),
('b8c42bbd-fc1a-4e03-bde5-99106d2fe2b1', 'e1389007-141c-4f43-9a03-1ddb8c153b32', 'Центральный'),
('7c72e606-da68-479d-a65b-a2833e74f6ed', 'bdbc5317-ea1f-492c-ade4-d0f5c018e00e', 'Невский'),
('3749ade5-05e2-4cc4-b350-9f834d2bec45', 'bdbc5317-ea1f-492c-ade4-d0f5c018e00e', 'Московский'),
('f351aa0d-6cc2-49c4-a2b1-c48b5eb7dfca', 'bdbc5317-ea1f-492c-ade4-d0f5c018e00e', 'Курортный'),
('fbbd5984-9ecb-4274-be31-34496a7daf94', 'bdbc5317-ea1f-492c-ade4-d0f5c018e00e', 'Красногвардейский'),
('6668f548-725e-4389-b932-6605a732250e', 'bdbc5317-ea1f-492c-ade4-d0f5c018e00e', 'Колпинский');
