CREATE TABLE IF NOT EXISTS "users" (
	"username"		TEXT NOT NULL,
	"id"			BLOB NOT NULL PRIMARY KEY,
	"discriminator"	BLOB NOT NULL,
	"afkStatus"		TEXT DEFAULT "False" NOT NULL,
	"afkMessage"	TEXT DEFAULT "No message set" NOT NULL
);
